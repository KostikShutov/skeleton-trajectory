class Command:
    def __init__(self, steering: float, speed: float) -> None:
        self.steering = steering
        self.speed = speed

    def __eq__(self, other) -> bool:
        return self.steering == other.steering \
            and self.speed == other.speed

    def __repr__(self) -> str:
        return '(' + str(self.steering) \
            + ', ' + str(self.speed) \
            + ')'

    def __str__(self) -> str:
        return '(steering: ' + str(self.steering) \
            + ', speed: ' + str(self.speed) \
            + ')'
