from collections.abc import Iterable
from components.coordinate.Coordinate import Coordinate
from components.coordinate.State import State


class CoordinateParser:
    def parse(self, data: Iterable) -> list[Coordinate]:
        coordinates: list[Coordinate] = []

        for item in data:
            if 'yaw' in item and 'steering' in item and 'speed' in item:
                state: State = State(
                    yaw=float(item['yaw']),
                    steering=float(item['steering']),
                    speed=float(item['speed']),
                )
            else:
                state: None = None

            coordinates.append(Coordinate(
                x=float(item['x']),
                y=float(item['y']),
                state=state,
            ))

        return coordinates
