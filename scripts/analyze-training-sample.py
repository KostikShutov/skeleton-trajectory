import json
from tqdm import tqdm
from collections import Counter
from collections.abc import Iterable
from components.command.CommandTransformer import CommandTransformer
from components.coordinate.Coordinate import Coordinate
from components.coordinate.CoordinateParser import CoordinateParser
from components.coordinate.CoordinateTransformer import CoordinateTransformer
from components.part.PartTransformer import PartTransformer
from components.command.Command import Command
from components.part.Part import Part
from generator.TrainHelper import TrainHelper
from utils.Utils import parseArgs
from utils.Math import distanceBetweenPoints


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


def analyzeTrainingSample(trainX: list[list[float]], trainY: list[list[float]]) -> None:
    print('---Analysis---')
    analysis: dict = {}
    emptyMessage: bool = True

    for listX, listY in zip(trainX, trainY):
        keyX: str = '_'.join([str(round(x, 2)) for x in listX])

        if keyX not in analysis:
            analysis[keyX] = []

        analysis[keyX].append(listY)

    for keyX, listsY in tqdm(analysis.items(), desc='Analyzing training sample'):
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
        print('No anomalies')


def printStatistics(items: list[tuple[Part, Command]]) -> None:
    print('---Statistics---')
    steerings: list[int] = []
    yaws: list[int] = []
    distances: list[float] = []

    for part, command in tqdm(items, desc='Printing statistics'):
        steerings.append(round(command.steering))
        yaws.append(round(part.yaw))
        coordinates: list[Coordinate] = part.coordinates
        distance: float = round(distanceBetweenPoints([Coordinate(x=0.0, y=0.0)] + [coordinates[0]]), 2)
        distances.append(distance)

    print('Steerings:')
    for steering, count in Counter(sorted(steerings)).items():
        print(f'{steering} [deg] ({count})')

    print('Yaws:')
    for yaw, count in Counter(sorted(yaws)).items():
        print(f'{yaw} [deg] ({count})')

    print('Distances:')
    for distance, count in Counter(sorted(distances)).items():
        print(f'{distance} [m] ({count})')


def main() -> None:
    args: any = parseArgs()
    modelDirectory: str = 'model/' + args.model + '/'
    modelFile: str = args.file

    with open(modelDirectory + modelFile + '.json') as file:
        course: Iterable = json.load(file)
        course: list[Coordinate] = getCoordinateParser().parse(course)

    trainHelper: TrainHelper = getTrainHelper()
    items: list[tuple[Part, Command]] = trainHelper.createTrainingItems(course)
    trainX, trainY = trainHelper.presentTrainingItems(items)
    analyzeTrainingSample(trainX, trainY)
    printStatistics(items)


if __name__ == '__main__':
    main()
