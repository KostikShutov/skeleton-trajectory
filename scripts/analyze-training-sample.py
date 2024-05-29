import os
import json
from tqdm import tqdm
from collections import Counter
from collections.abc import Iterable
from collections import defaultdict
from components.command.CommandTransformer import CommandTransformer
from components.coordinate.Coordinate import Coordinate
from components.coordinate.CoordinateParser import CoordinateParser
from components.coordinate.CoordinateTransformer import CoordinateTransformer
from components.part.PartTransformer import PartTransformer
from components.command.Command import Command
from components.part.Part import Part
from generator.TrainHelper import TrainHelper
from helpers.Utility import parseArgs


def getCoordinateParser() -> CoordinateParser:
    return CoordinateParser()


def getTrainHelper() -> TrainHelper:
    commandTransformer = CommandTransformer()
    partTransformer = PartTransformer()
    coordinateTransformer = CoordinateTransformer()

    return TrainHelper(
        coordinateTransformer=coordinateTransformer,
        commandTransformer=commandTransformer,
        partTransformer=partTransformer,
    )


def analyzeTrainingSample(trainX: list[list[float]],
                          trainSteeringY: list[list[float]],
                          trainSpeedY: list[list[float]]) -> None:
    print('---Analysis---')
    analysisSteering: dict = defaultdict(list)
    analysisSpeed: dict = defaultdict(list)

    for listX, listSteeringY, listSpeedY in zip(trainX, trainSteeringY, trainSpeedY):
        keyX: str = '_'.join([str(round(x, 2)) for x in listX])
        analysisSteering[keyX].append(listSteeringY)
        analysisSpeed[keyX].append(listSpeedY)

    doAnalysis(analysis=analysisSteering, name='steering')
    doAnalysis(analysis=analysisSpeed, name='speed')


def doAnalysis(analysis: dict, name: str) -> None:
    emptyMessage: bool = True

    for keyX, listsY in tqdm(analysis.items(), desc='Analyzing ' + name + ' training sample'):
        keysY: list = []

        for listY in listsY:
            keyY: str = '_'.join([str(round(y, 2)) for y in listY])
            keysY.append(keyY)

        counter: Counter = Counter(keysY)

        if len(counter) > 1:
            emptyMessage: bool = False
            print(f"Anomaly: {keyX}")

            for keyY in counter.keys():
                print(f"    {keyY}")

    if emptyMessage:
        print('No ' + name + ' anomalies')


def main() -> None:
    args: any = parseArgs()
    modelName: str = args.model
    modelDirectory: str = 'model/' + modelName + '/'
    modelFile: str = modelDirectory + args.file + '.json'

    print('---Running ' + os.path.basename(__file__) + '---')
    print('Model file: ' + modelFile)

    with open(modelFile) as file:
        course: Iterable = json.load(file)
        course: list[Coordinate] = getCoordinateParser().parse(course)

    trainHelper: TrainHelper = getTrainHelper()
    items: list[tuple[Part, Command]] = trainHelper.createItems(course)
    trainX, trainSteeringY, trainSpeedY = trainHelper.presentItems(items)
    analyzeTrainingSample(trainX, trainSteeringY, trainSpeedY)


if __name__ == '__main__':
    main()
