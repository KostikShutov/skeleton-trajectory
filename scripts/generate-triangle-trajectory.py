import json
import math
from components.coordinate.Coordinate import Coordinate
from utils.Utils import createDirectory, parseArgs


def generateTrajectory(min: float, max: float, points: int) -> list[object]:
    side: float = max - min
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
            c2=Coordinate(x=side / 2, y=math.sqrt(3) * side / 2),
            points=points,
    )[:-1]:
        result.append({
            'x': c.x,
            'y': c.y,
        })

    for c in interpolatePoints(
            c1=Coordinate(x=side / 2, y=math.sqrt(3) * side / 2),
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
    modelFile: str = args.file
    side: float = float(args.side)
    points: int = args.points

    trajectory: list[object] = generateTrajectory(min=0.0, max=side, points=points)
    createDirectory(directory=modelDirectory)

    saveTrajectory(
        path=modelDirectory + modelFile + '.json',
        trajectory=trajectory,
    )


if __name__ == '__main__':
    main()
