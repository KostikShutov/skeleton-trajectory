from components.coordinate.State import State


class Coordinate:
    def __init__(self, x: float, y: float, state: State = None) -> None:
        self.x = round(x, 10)
        self.y = round(y, 10)
        self.state = state

    def __eq__(self, other) -> bool:
        return self.x == other.x \
            and self.y == other.y \
            and self.state == other.state

    def __repr__(self) -> str:
        return '(' + str(self.x) \
            + ', ' + str(self.y) \
            + ', ' + str(self.state) \
            + ')'

    def __str__(self) -> str:
        return '(x: ' + str(self.x) \
            + ', y: ' + str(self.y) \
            + ', state: ' + str(self.state) \
            + ')'
