import os
import json
import math
import random
import pandas as pd
import matplotlib.pyplot as plt
from components.coordinate.Coordinate import Coordinate
from components.coordinate.State import State
from components.config.Config import Config
from components.command.CommandTransformer import CommandTransformer
from components.coordinate.CoordinateTransformer import CoordinateTransformer
from components.part.PartTransformer import PartTransformer
from generator.TrainHelper import TrainHelper
from helpers.Utility import parseArgs
from helpers.Math import normalizeAngle, distanceBetweenPoints


def getRandomTrainPart(path: str) -> list[Coordinate]:
    with open(path, 'r') as file:
        items: list = json.load(file)

    count: int = 7
    start: int = random.randint(0, len(items) - count)
    items: list = items[start:start + count]
    result: list[Coordinate] = []

    for item in items:
        result.append(Coordinate(
            x=item['x'],
            y=item['y'],
            state=State(
                yaw=item['yaw'],
                steering=item['steering'],
                speed=item['speed'],
            ),
        ))

    return result


def addPlot(course: list[Coordinate], ax: any) -> None:
    pointsX: list[float] = []
    pointsY: list[float] = []
    breaksX: list[float] = []
    breaksY: list[float] = []

    oldCoordinate: Coordinate | None = None

    for i, newCoordinate in enumerate(course):
        if i == len(course) - 1:
            break

        if oldCoordinate is not None:
            breaksX.append(oldCoordinate.x)
            breaksY.append(oldCoordinate.y)

            x: float = oldCoordinate.x  # [m]
            y: float = oldCoordinate.y  # [m]
            yaw: float = math.radians(oldCoordinate.state.yaw)  # [rad]
            steering: float = math.radians(oldCoordinate.state.steering)  # [rad]
            speed: float = oldCoordinate.state.speed  # [m/s]
            duration: float = 0.01  # [s]
            j: int = 0

            while True:
                pointsX.append(x)
                pointsY.append(y)

                x += speed * math.cos(yaw) * duration  # [m]
                y += speed * math.sin(yaw) * duration  # [m]
                yaw += math.tan(steering) * (speed / Config.LENGTH) * duration  # [rad]
                yaw: float = normalizeAngle(yaw)  # [rad]
                j += 1

                if distanceBetweenPoints([Coordinate(x, y), newCoordinate]) <= 0.02:  # [m]
                    break

            high: int = math.ceil((j / 2) + 1)
            low: int = math.ceil(j / 2)

            ax.annotate(
                text='',
                xy=(pointsX[-high], pointsY[-high]),
                xytext=(pointsX[-low], pointsY[-low]),
                arrowprops=dict(arrowstyle='->', color='r', lw=1.2),
            )

            ax.text(
                x=(pointsX[-high] + pointsX[-low]) / 2,
                y=(pointsY[-high] + pointsY[-low]) / 2,
                s=f'{oldCoordinate.state.speed} m/s',
                fontsize=10,
                color='black',
            )

            breaksX.append(newCoordinate.x)
            breaksY.append(newCoordinate.y)

        oldCoordinate: Coordinate = newCoordinate

    ax.plot(pointsX, pointsY, marker='o', markersize=1, color='red')
    ax.plot(breaksX, breaksY, marker='o', markersize=5, color='blue', linestyle='')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(True)
    ax.axis('equal')


def printTrainPart(course: list[Coordinate], ax: any) -> None:
    trainHelper: TrainHelper = TrainHelper(
        coordinateTransformer=CoordinateTransformer(),
        commandTransformer=CommandTransformer(),
        partTransformer=PartTransformer(),
    )

    items: list = trainHelper.createItems(course=course)
    trainX, trainSteeringY, trainSpeedY = trainHelper.presentItems(items=items)

    df = pd.DataFrame(data=trainX, columns=['length 1', 'length 2', 'angle', 'yaw'])
    df.insert(0, '№', [str(i) for i in range(1, len(df) + 1)])  # noqa
    df['output steering'] = [item[0] for item in trainSteeringY]
    df['output speed'] = [item[0] for item in trainSpeedY]
    df = df.round(2)
    ax.axis('off')
    table = ax.table(cellText=df.values, colLabels=df.columns, loc='center')
    table.auto_set_column_width(col=list(range(len(df.columns))))
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)


def main() -> None:
    args: any = parseArgs()
    modelFile: str = 'model/' + args.model + '/' + args.file + '.json'

    print('---Running ' + os.path.basename(__file__) + '---')
    print('Model file: ' + modelFile)

    fig, (ax1, ax2) = plt.subplots(2, 1)
    coordinates: list[Coordinate] = getRandomTrainPart(path=modelFile)
    addPlot(course=coordinates, ax=ax1)
    printTrainPart(course=coordinates, ax=ax2)
    plt.show()


if __name__ == '__main__':
    main()
