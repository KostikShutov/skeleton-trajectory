import math
import random
from components.config.Config import Config
from components.model.StrategyInterface import StrategyInterface


class StaticAggressiveStrategy(StrategyInterface):
    def modifyCoordinate(self, x: float, y: float, yaw: float, speed: float) -> tuple[float, float]:
        for _ in range(random.randint(10, 20)):
            x += speed * math.cos(yaw) * Config.DURATION  # [m]
            y += speed * math.sin(yaw) * Config.DURATION  # [m]

        return x, y

    def generateSteering(self) -> float:
        return math.radians(random.choice([
            float(random.randint(
                int(Config.MIN_STEERING),
                -35,
            )),
            float(random.randint(
                35,
                int(Config.MAX_STEERING),
            )),
        ]))

    def generateSpeed(self, steering: float) -> float:
        return Config.MAX_SPEED

    def generatePoints(self, speed: float) -> int:
        return random.randint(10, 20)
