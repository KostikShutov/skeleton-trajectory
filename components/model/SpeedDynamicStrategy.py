import math
import random
from components.config.Config import Config
from components.model.StrategyInterface import StrategyInterface


class SpeedDynamicStrategy(StrategyInterface):
    def modifyCoordinate(self, x: float, y: float, yaw: float, speed: float) -> tuple[float, float]:
        if speed <= 0.2:
            return x, y

        points: int = random.randint(35, 60)

        for _ in range(points):
            x += speed * math.cos(yaw) * Config.DURATION  # [m]
            y += speed * math.sin(yaw) * Config.DURATION  # [m]

        return x, y

    def generateSteering(self) -> float:
        return math.radians(float(random.randint(
            int(Config.MIN_STEERING),
            int(Config.MAX_STEERING),
        )))

    def generateSpeed(self, steering: float) -> float:
        steering: float = math.degrees(steering)  # [deg]
        steering: float = abs(steering)  # [deg]

        if 40.0 < steering <= Config.MAX_STEERING:
            return 0.1

        if 35.0 < steering <= 40.0:
            return 0.15

        if 30.0 < steering <= 35.0:
            return 0.2

        if 25.0 < steering <= 30.0:
            return 0.25

        if 20.0 < steering <= 25.0:
            return 0.3

        if 15.0 < steering <= 20.0:
            return 0.45

        return Config.MAX_SPEED

    def generatePoints(self, speed: float) -> int:
        if speed <= 0.2:
            return random.randint(20, 55)

        return 5
