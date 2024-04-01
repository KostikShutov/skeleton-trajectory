import os
import json
import pickle
import visualkeras
from datetime import datetime
from collections.abc import Iterable
from tf_keras.models import Sequential
from tf_keras.utils import plot_model
from tf_keras.callbacks import EarlyStopping, TensorBoard
from keras_visualizer import visualizer
from sklearn.preprocessing import MinMaxScaler
from components.command.Command import Command
from components.coordinate.Coordinate import Coordinate
from components.coordinate.CoordinateParser import CoordinateParser
from components.part.Part import Part
from components.model.Model import Model
from generator.TrainHelper import TrainHelper
from helpers.Utility import createDirectory


class TrainService:
    def __init__(self, coordinateParser: CoordinateParser,
                 trainHelper: TrainHelper) -> None:
        self.coordinateParser = coordinateParser
        self.trainHelper = trainHelper

    def train(self, modelName: str) -> None:
        modelDirectory: str = 'model/' + modelName + '/'

        with open(modelDirectory + 'train.json', 'r') as file:
            course: Iterable = json.load(file)

        course: list[Coordinate] = self.coordinateParser.parse(course)
        items: list[tuple[Part, Command]] = self.trainHelper.createItems(course)
        trainX, trainSteeringY, trainSpeedY = self.trainHelper.presentItems(items)

        self.__trainModel(trainX, trainSteeringY, modelDirectory + 'steering/')
        self.__trainModel(trainX, trainSpeedY, modelDirectory + 'speed/')

    def __trainModel(self, trainX: list[list[float]], trainY: list[list[float]], modelDirectory: str) -> None:
        tensorboardDir: str = 'tensorboard/' + modelDirectory + datetime.now().strftime('%Y-%m-%d_%H:%M:%S.%f')
        tensorboardCallback: TensorBoard = TensorBoard(log_dir=tensorboardDir, histogram_freq=1)
        earlyStopping: EarlyStopping = EarlyStopping(patience=3)

        xScaler: MinMaxScaler = MinMaxScaler()
        yScaler: MinMaxScaler = MinMaxScaler()
        model: Sequential = Model().getModel()

        model.fit(x=xScaler.fit_transform(trainX),
                  y=yScaler.fit_transform(trainY),
                  epochs=50,
                  validation_split=0.2,
                  callbacks=[tensorboardCallback, earlyStopping])

        self.__saveModel(model, xScaler, yScaler, modelDirectory)

    def __saveModel(self, model: Sequential,
                    xScaler: MinMaxScaler,
                    yScaler: MinMaxScaler,
                    modelDirectory: str) -> None:
        createDirectory(modelDirectory)
        json: str = model.to_json()

        with open(modelDirectory + 'model.json', 'w') as file:
            file.write(json)

        model.save_weights(modelDirectory + 'model.h5')

        with open(modelDirectory + 'x_scaler.pickle', 'wb') as file:
            pickle.dump(xScaler, file)

        with open(modelDirectory + 'y_scaler.pickle', 'wb') as file:
            pickle.dump(yScaler, file)

        plot_model(model, to_file=modelDirectory + 'model.png', show_shapes=True, show_layer_names=False)
        visualizer(model, file_name=modelDirectory + 'graph', file_format='png')
        os.remove(modelDirectory + 'graph')
        visualkeras.layered_view(model, legend=True, to_file=modelDirectory + 'view.png')
