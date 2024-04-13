from components.model.ModelName import ModelName
from components.model.StaticSmoothlyStrategy import StaticSmoothlyStrategy
from components.model.StaticAggressiveStrategy import StaticAggressiveStrategy
from components.model.SpeedDynamicStrategy import SpeedDynamicStrategy
from components.model.SpeedSlowStrategy import SpeedSlowStrategy
from components.model.SpeedWeeklyStrategy import SpeedWeeklyStrategy
from components.model.StrategyInterface import StrategyInterface


class StrategyResolver:
    def resolve(self, modelName: ModelName) -> StrategyInterface:
        if modelName == ModelName.STATIC_SMOOTHLY:
            return StaticSmoothlyStrategy()

        if modelName == ModelName.STATIC_AGGRESSIVE:
            return StaticAggressiveStrategy()

        if modelName == ModelName.SPEED_DYNAMIC:
            return SpeedDynamicStrategy()

        if modelName == ModelName.SPEED_SLOW:
            return SpeedSlowStrategy()

        if modelName == ModelName.SPEED_WEEKLY:
            return SpeedWeeklyStrategy()

        raise NotImplementedError('Model not implemented')
