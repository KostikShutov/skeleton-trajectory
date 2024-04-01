import os
import json
from components.coordinate.Coordinate import Coordinate
from helpers.Utility import createDirectory, parseArgs


def generateTrajectory(points: int) -> list[object]:
    result: list[object] = []

    for c in interpolatePoints(
            c1=Coordinate(x=0.0, y=0.0),
            c2=Coordinate(x=3.0, y=0.0),
            points=points,
    )[:-1]:
        result.append({
            'x': c.x,
            'y': c.y,
        })

    for c in interpolatePoints(
            c1=Coordinate(x=3.0, y=0.0),
            c2=Coordinate(x=3.0, y=0.5),
            points=points,
    )[:-1]:
        result.append({
            'x': c.x,
            'y': c.y,
        })

    for c in interpolatePoints(
            c1=Coordinate(x=3.0, y=0.5),
            c2=Coordinate(x=0.0, y=0.5),
            points=points,
    )[:-1]:
        result.append({
            'x': c.x,
            'y': c.y,
        })

    for c in interpolatePoints(
            c1=Coordinate(x=0.0, y=0.5),
            c2=Coordinate(x=0.0, y=0.0),
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
    points: int = args.points

    print('---Running ' + os.path.basename(__file__) + '---')
    print('Model file: ' + modelFile)
    print('Points: ' + str(points))

    trajectory: list[object] = generateTrajectory(points=points)
    createDirectory(directory=modelDirectory)
    saveTrajectory(path=modelFile, trajectory=trajectory)


if __name__ == '__main__':
    main()
