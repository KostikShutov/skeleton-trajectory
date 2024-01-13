import os
import json
import pickle
import visualkeras
import tensorflow as tf
from datetime import datetime
from collections.abc import Iterable
from keras.models import Sequential
from keras.utils import plot_model
from keras.callbacks import EarlyStopping
from keras_visualizer import visualizer
from sklearn.preprocessing import MinMaxScaler
from components.command.Command import Command
from components.coordinate.Coordinate import Coordinate
from components.coordinate.CoordinateParser import CoordinateParser
from components.part.Part import Part
from components.model.Model import Model
from generator.TrainHelper import TrainHelper


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
        items: list[tuple[Part, Command]] = self.trainHelper.createTrainingItems(course)
        trainX, trainY = self.trainHelper.presentTrainingItems(items)

        tensorboardDir: str = 'tensorboard/' + datetime.now().strftime('%Y-%m-%d_%H:%M:%S.%f')
        tensorboardCallback: any = tf.keras.callbacks.TensorBoard(log_dir=tensorboardDir, histogram_freq=1)
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
