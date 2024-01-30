import os
import json
import math
from components.coordinate.Coordinate import Coordinate
from components.part.Part import Part
from components.part.PartTransformer import PartTransformer
from helpers.Utility import createDirectory, parseArgs


def generateTrajectory(distance: float, points: int) -> list[object]:
    coordinates: list[Coordinate] = []
    newCoordinates: list[Coordinate] = []
    result: list[object] = [{
        'x': 0.0,
        'y': 0.0,
    }]

    for i in (4, 5, 0, 1, 2, 3):
        coordinates.append(Coordinate(
            x=distance * math.cos(2 * math.pi * i / 6),
            y=distance * math.sin(2 * math.pi * i / 6),
        ))

    for i in range(len(coordinates) - 1):
        for c in interpolatePoints(
                c1=coordinates[i],
                c2=coordinates[i + 1],
                points=points,
        )[:-1]:
            newCoordinates.append(c)

    for c in interpolatePoints(
            c1=coordinates[len(coordinates) - 1],
            c2=coordinates[0],
            points=points,
    ):
        newCoordinates.append(c)

    for c in PartTransformer().normalizeToZero(Part(coordinates=newCoordinates, yaw=0.0)).coordinates:
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
