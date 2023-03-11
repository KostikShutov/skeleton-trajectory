class State:
    def __init__(self, yaw: float, steering: float, speed: float) -> None:
        self.yaw = round(yaw, 10)
        self.steering = round(steering, 10)
        self.speed = round(speed, 10)

    def __eq__(self, other) -> bool:
        return self.yaw == other.yaw \
            and self.steering == other.steering \
            and self.speed == other.speed

    def __repr__(self) -> str:
        return '(' + str(self.yaw) \
            + ', ' + str(self.steering) \
            + ', ' + str(self.speed) \
            + ')'

    def __str__(self) -> str:
        return '(yaw: ' + str(self.yaw) \
            + ', steering: ' + str(self.steering) \
            + ', speed: ' + str(self.speed) \
            + ')'
