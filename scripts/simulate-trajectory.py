import os
import json
import matplotlib.pyplot as plt
from collections.abc import Iterable
from components.coordinate.Coordinate import Coordinate
from helpers.Utility import parseArgs
from json.decoder import JSONDecodeError


def loadItems(path: str) -> Iterable | None:
    try:
        with open(path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print('Notice: path "' + path + '" does not exist')
        return None
    except JSONDecodeError:
        print('Warning: json in "' + path + '" is not valid')
        return None


def addRealPlot(path: str) -> None:
    items: Iterable | None = loadItems(path)

    if items is None:
        return

    pointsX: list[float] = []
    pointsY: list[float] = []

    for item in items:
        coordinate: Coordinate = Coordinate(
            x=item['x'],
            y=item['y'],
        )

        pointsX.append(coordinate.x)
        pointsY.append(coordinate.y)

    plt.plot(pointsX, pointsY, marker='o', markersize=10, color='blue', linestyle='')


def addPredictedPlot(path: str) -> None:
    items: Iterable | None = loadItems(path)

    if items is None:
        return

    predictedPointsX: list[float] = []
    predictedPointsY: list[float] = []

    for item in items:
        coordinate: Coordinate = Coordinate(
            x=item['x'],
            y=item['y'],
        )

        predictedPointsX.append(coordinate.x)
        predictedPointsY.append(coordinate.y)

    plt.plot(predictedPointsX, predictedPointsY, marker='o', markersize=1, color='red')


def showPlot() -> None:
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()


def main() -> None:
    args: any = parseArgs()
    modelDirectory: str = 'model/' + args.model + '/'
    realModelFile: str = modelDirectory + args.file + '.json'
    predictedModelFile: str = modelDirectory + args.file + '.predict.json'

    print('---Running ' + os.path.basename(__file__) + '---')
    print('Real model file: ' + realModelFile)
    print('Predicted model file: ' + predictedModelFile)

    addRealPlot(path=realModelFile)
    addPredictedPlot(path=predictedModelFile)
    showPlot()


if __name__ == '__main__':
    main()
