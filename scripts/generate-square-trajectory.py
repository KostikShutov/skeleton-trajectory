import os
import json
from components.coordinate.Coordinate import Coordinate
from helpers.Utility import createDirectory, parseArgs


def generateTrajectory(distance: float, points: int) -> list[object]:
    min: float = 0.0
    max: float = distance
    result: list[object] = []

    for c in interpolatePoints(
            c1=Coordinate(x=min, y=min),
            c2=Coordinate(x=max, y=min),
            points=points,
    )[:-1]:
        result.append({
            'x': c.x,
            'y': c.y,
        })

    for c in interpolatePoints(
            c1=Coordinate(x=max, y=min),
            c2=Coordinate(x=max, y=max),
            points=points,
    )[:-1]:
        result.append({
            'x': c.x,
            'y': c.y,
        })

    for c in interpolatePoints(
            c1=Coordinate(x=max, y=max),
            c2=Coordinate(x=min, y=max),
            points=points,
    )[:-1]:
        result.append({
            'x': c.x,
            'y': c.y,
        })

    for c in interpolatePoints(
            c1=Coordinate(x=min, y=max),
            c2=Coordinate(x=min, y=min),
            points=points,
    ):
        result.append({
            'x': c.x,
            'y': c.y,
        })

    return result


def interpolatePoints(c1: Coordinate, c2: Coordinate, points: int) -> list[Coordinate]:
    if points <= 2:
        return [c1, c2]

    stepX: float = (c2.x - c1.x) / (points - 1) if points > 1 else 0
    stepY: float = (c2.y - c1.y) / (points - 1) if points > 1 else 0

    return [Coordinate(x=c1.x + i * stepX, y=c1.y + i * stepY) for i in range(points)]


def saveTrajectory(path: str, trajectory: list[object]) -> None:
    with open(path, 'w') as file:
        file.write(json.dumps(trajectory))
        file.write('\n')


def main() -> None:
    args: any = parseArgs()
    modelDirectory: str = 'model/' + args.model + '/'
    modelFile: str = modelDirectory + args.file + '.json'
    distance: int = args.distance
    points: int = args.points

    print('---Running ' + os.path.basename(__file__) + '---')
    print('Model file: ' + modelFile)
    print('Distance: ' + str(distance))
    print('Points: ' + str(points))

    trajectory: list[object] = generateTrajectory(distance=float(distance), points=points)
    createDirectory(directory=modelDirectory)
    saveTrajectory(path=modelFile, trajectory=trajectory)


if __name__ == '__main__':
    main()
