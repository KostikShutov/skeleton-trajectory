import math
import random
from components.config.Config import Config
from components.model.StrategyInterface import StrategyInterface


class StaticSmoothlyStrategy(StrategyInterface):
    def modifyCoordinate(self, x: float, y: float, yaw: float, speed: float) -> tuple[float, float]:
        return x, y

    def generateSteering(self) -> float:
        return math.radians(float(random.randint(
            int(Config.MIN_STEERING),
            int(Config.MAX_STEERING),
        )))

    def generateSpeed(self, steering: float) -> float:
        return Config.MAX_SPEED

    def generatePoints(self, speed: float) -> int:
        return random.randint(10, 40)
