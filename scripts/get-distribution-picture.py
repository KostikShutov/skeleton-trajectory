import os
import json
import numpy as np
import matplotlib.pyplot as plt
from collections.abc import Iterable
from helpers.Utility import parseArgs


def addSteerings(steerings: dict) -> None:
    plt.figure()
    plt.xticks(ticks=np.arange(-45, 46, 1), rotation=90, fontsize=8)
    plt.bar(x=steerings.keys(), height=steerings.values())  # noqa
    plt.title('Распределение угла поворота рулевого колеса')
    plt.xlabel('Значение')
    plt.ylabel('Количество')


def addSpeeds(speeds: dict) -> None:
    plt.figure()
    plt.xticks(ticks=np.arange(0.1, 0.55, 0.05))
    plt.bar(x=speeds.keys(), height=speeds.values(), width=0.03)  # noqa
    plt.title('Распределение скорости движения')
    plt.xlabel('Значение')
    plt.ylabel('Количество')


def distribute(path: str) -> None:
    with open(path, 'r') as file:
        items: Iterable = json.load(file)

    steerings: dict = {}
    speeds: dict = {}

    for item in items:
        steering: int = int(round(item['steering'], 0))
        steerings[steering] = steerings.get(steering, 0) + 1

        speed: float = float(round(item['speed'], 2))
        speeds[speed] = speeds.get(speed, 0) + 1

    addSteerings(steerings)
    addSpeeds(speeds)
    plt.show()


def main() -> None:
    args: any = parseArgs()
    modelFile: str = 'model/' + args.model + '/' + args.file + '.json'

    print('---Running ' + os.path.basename(__file__) + '---')
    print('Model file: ' + modelFile)

    distribute(path=modelFile)


if __name__ == '__main__':
    main()
