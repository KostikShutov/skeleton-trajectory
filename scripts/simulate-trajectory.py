import math
import json
import matplotlib.pyplot as plt
from collections.abc import Iterable
from components.config.Config import Config
from components.coordinate.Coordinate import Coordinate
from components.coordinate.State import State
from utils.Utils import parseArgs
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

    plt.plot(pointsX, pointsY, marker='o', markersize=6, color='blue', label='Original', linestyle='')


def addPredictedPlot(path: str) -> None:
    items: Iterable | None = loadItems(path)

    if items is None:
        return

    predictedPointsX: list[float] = []
    predictedPointsY: list[float] = []
    trainedPointsX: list[float] = []
    trainedPointsY: list[float] = []
    duration: float = 0.0  # [s]

    for item in items:
        coordinate: Coordinate = Coordinate(
            x=item['x'],
            y=item['y'],
        )

        predictedPointsX.append(coordinate.x)
        predictedPointsY.append(coordinate.y)
        duration += Config.SIMULATE_DURATION

        if round(duration, 1) == Config.GENERATE_DURATION:
            trainedPointsX.append(coordinate.x)
            trainedPointsY.append(coordinate.y)
            duration = 0.0

    plt.plot(predictedPointsX, predictedPointsY, marker='o', markersize=1, color='red', label='Predicted (dt = 0.01)')
    plt.plot(trainedPointsX, trainedPointsY, marker='o', markersize=1, color='green', label='Points (dT = 0.1)',
             linestyle='')


def showPlot() -> None:
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.legend()
    plt.show()


def main() -> None:
    args: any = parseArgs()
    modelDirectory: str = 'model/' + args.model + '/'
    modelFile: str = args.file

    addRealPlot(path=modelDirectory + modelFile + '.json')
    addPredictedPlot(path=modelDirectory + modelFile + '.predict.json')
    showPlot()


if __name__ == '__main__':
    main()
