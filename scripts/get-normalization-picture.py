from components.coordinate.Coordinate import Coordinate
from helpers.Math import rotatePoints
from helpers.Utility import removeFirst
import matplotlib.pyplot as plt


def init(subplot: any) -> list[Coordinate]:
    coordinates: list[Coordinate] = [
        Coordinate(x=1.0, y=0.0),
        Coordinate(x=1.5, y=0.8660254038),
        Coordinate(x=1.0, y=1.7320508076),
    ]

    subplot.plot(
        [c.x for c in coordinates],
        [c.y for c in coordinates],
        marker='o',
        markersize=1,
        color='blue',
    )

    subplot.axis('square')
    subplot.grid(True)
    subplot.set_title('1')

    return coordinates


def move(coordinates: list[Coordinate], subplot: any) -> list[Coordinate]:
    first: Coordinate = coordinates[0]
    normalized: list[Coordinate] = []

    for coordinate in coordinates:
        normalized.append(Coordinate(
            x=coordinate.x - first.x,
            y=coordinate.y - first.y,
        ))

    subplot.plot(
        [c.x for c in normalized],
        [c.y for c in normalized],
        marker='o',
        markersize=1,
        color='blue',
    )

    subplot.axis('square')
    subplot.grid(True)
    subplot.set_title('2')

    return normalized


def rotate(normalized: list[Coordinate], subplot: any) -> list[Coordinate]:
    normalized, _ = rotatePoints(normalized)

    subplot.plot(
        [c.x for c in normalized],
        [c.y for c in normalized],
        marker='o',
        markersize=1,
        color='blue',
    )

    subplot.axis('square')
    subplot.grid(True)
    subplot.set_title('3')

    return normalized


def remove(normalized: list[Coordinate], subplot: any) -> None:
    normalized: list[Coordinate] = removeFirst(normalized)

    subplot.plot(
        [c.x for c in normalized],
        [c.y for c in normalized],
        marker='o',
        markersize=1,
        color='blue',
    )

    subplot.axis('square')
    subplot.grid(True)
    subplot.set_title('4')


def main() -> None:
    fig, axs = plt.subplots(nrows=1, ncols=4, sharex=True, sharey=True)

    coordinates: list[Coordinate] = init(subplot=axs[0])
    coordinates: list[Coordinate] = move(coordinates=coordinates, subplot=axs[1])
    coordinates: list[Coordinate] = rotate(normalized=coordinates, subplot=axs[2])
    remove(normalized=coordinates, subplot=axs[3])

    plt.show()


if __name__ == '__main__':
    main()
