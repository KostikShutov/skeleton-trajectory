import math
from components.coordinate.Coordinate import Coordinate


def distanceBetweenPoints(coordinates: list[Coordinate]) -> float:
    distance: float = 0.0

    for i in range(len(coordinates) - 1):
        c1: Coordinate = coordinates[i]
        c2: Coordinate = coordinates[i + 1]
        distance += math.sqrt((c2.x - c1.x) ** 2 + (c2.y - c1.y) ** 2)

    return distance


def angleBetweenVectorAndX(first: Coordinate, second: Coordinate) -> float:
    return math.atan2(
        second.y - first.y,
        second.x - first.x,
    )


def rotatePoints(coordinates: list[Coordinate]) -> tuple[list[Coordinate], float]:
    if len(coordinates) <= 1:
        raise ValueError('Must provide >= 2 coordinates')

    if coordinates[0].x != 0.0 and coordinates[0].y != 0.0:
        raise ValueError('First coordinate must be (0, 0)')

    angle: float = angleBetweenVectorAndX(coordinates[0], coordinates[1])  # [rad]
    angle: float = -angle  # [rad]
    result: list[Coordinate] = []

    for coordinate in coordinates:
        result.append(Coordinate(
            x=coordinate.x * math.cos(angle) - coordinate.y * math.sin(angle),
            y=coordinate.x * math.sin(angle) + coordinate.y * math.cos(angle),
        ))

    return result, math.degrees(angle)  # [deg]


def normalizeAngle(angle: float) -> float:
    while angle > math.pi:
        angle -= 2.0 * math.pi

    while angle < -math.pi:
        angle += 2.0 * math.pi

    return angle  # [rad]
