from components.coordinate.Coordinate import Coordinate


class Part:
    def __init__(self, coordinates: list[Coordinate], yaw: float) -> None:
        self.coordinates = coordinates
        self.yaw = round(yaw, 10)

    def __eq__(self, other) -> bool:
        return self.coordinates == other.coordinates \
            and self.yaw == other.yaw

    def __repr__(self) -> str:
        return '(' + str(self.coordinates) \
            + ', ' + str(self.yaw) \
            + ')'

    def __str__(self) -> str:
        return '(coordinates: ' + str(self.coordinates) \
            + ', yaw: ' + str(self.yaw) \
            + ')'
