class StrategyInterface:
    def modifyCoordinate(self, x: float, y: float, yaw: float, speed: float) -> tuple[float, float]:
        pass

    def generateSteering(self) -> float:
        pass

    def generateSpeed(self, steering: float) -> float:
        pass

    def generatePoints(self, speed: float) -> int:
        pass
