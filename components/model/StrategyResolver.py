from components.model.ModelName import ModelName
from components.model.NormalStrategy import NormalStrategy
from components.model.AggressiveStrategy import AggressiveStrategy
from components.model.DynamicStrategy import DynamicStrategy
from components.model.StrategyInterface import StrategyInterface


class StrategyResolver:
    def resolve(self, modelName: str) -> StrategyInterface:
        if modelName == ModelName.NORMAL.value:
            return NormalStrategy()

        if modelName == ModelName.AGGRESSIVE.value:
            return AggressiveStrategy()

        if modelName == ModelName.DYNAMIC.value:
            return DynamicStrategy()

        raise NotImplementedError('Model not implemented')
