import os
import json
import matplotlib.pyplot as plt
from collections.abc import Iterable
from components.config.Config import Config
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


def addPredictedPlot(path: str, warm: bool) -> None:
    items: Iterable | None = loadItems(path)

    if items is None:
        return

    pointsX: list[float] = []
    pointsY: list[float] = []
    speed: list[float] = []

    for item in items:
        coordinate: Coordinate = Coordinate(
            x=item['x'],
            y=item['y'],
        )

        pointsX.append(coordinate.x)
        pointsY.append(coordinate.y)
        currentSpeed: float = item['speed']

        if warm and len(speed) > 0:
            lastSpeed: float = speed[-1]

            if currentSpeed != lastSpeed:
                count: int = 50
                delta: float = (currentSpeed - lastSpeed) / count

                for i in range(1, count):
                    speed[-i] = currentSpeed - i * delta

        speed.append(currentSpeed)

    if warm:
        plt.scatter(pointsX, pointsY, c=speed, cmap='Wistia', s=15, vmin=Config.MIN_SPEED, vmax=Config.MAX_SPEED)
        plt.plot(pointsX, pointsY, c='black', alpha=0.3)
        plt.colorbar(label='Скорость')
    else:
        plt.plot(pointsX, pointsY, marker='o', markersize=1, color='red')

    for i, item in enumerate(items):
        x = item['x']
        y = item['y']

        try:
            speed = round(item['speed'], 2)
        except KeyError:
            return

        if i % 80 == 0:
            plt.text(x, y, f'{speed} m/s', fontsize=10, color='black')


def showPlot() -> None:
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.axis('equal')
    plt.show()


def main() -> None:
    args: any = parseArgs()
    modelDirectory: str = 'model/' + args.model + '/'
    realModelFile: str = modelDirectory + args.file + '.json'
    predictedModelFile: str = modelDirectory + args.file + '.predict.json'
    warm: bool = bool(args.warm)

    print('---Running ' + os.path.basename(__file__) + '---')
    print('Real model file: ' + realModelFile)
    print('Predicted model file: ' + predictedModelFile)
    print('Warm: ' + str(warm))

    addRealPlot(path=realModelFile)
    addPredictedPlot(path=predictedModelFile, warm=warm)
    showPlot()


if __name__ == '__main__':
    main()
