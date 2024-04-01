import math
import random
from components.config.Config import Config
from components.model.StrategyInterface import StrategyInterface


class DynamicStrategy(StrategyInterface):
    def modifyCoordinate(self, x: float, y: float, yaw: float, speed: float) -> tuple[float, float]:
        return x, y

    def generateSteering(self) -> float:
        return math.radians(float(random.randint(
            int(Config.MIN_STEERING),
            int(Config.MAX_STEERING),
        )))

    def generateSpeed(self, steering: float) -> float:
        steering: float = math.degrees(steering)  # [deg]
        steering: float = abs(steering)  # [deg]

        if 35.0 < steering <= Config.MAX_STEERING:
            return random.uniform(0.1, 0.2)

        if 20.0 < steering <= 35.0:
            return random.uniform(0.2, 0.3)

        if 10.0 < steering <= 20.0:
            return random.uniform(0.3, 0.4)

        return random.uniform(0.4, Config.MAX_SPEED)

    def generatePoints(self, speed: float) -> int:
        return round((Config.MAX_SPEED / speed) * random.randint(10, 40))
