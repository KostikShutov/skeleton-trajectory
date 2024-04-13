from enum import Enum


class ModelName(Enum):
    STATIC_SMOOTHLY: str = 'static_smoothly'
    STATIC_AGGRESSIVE: str = 'static_aggressive'
    SPEED_DYNAMIC: str = 'speed_dynamic'
    SPEED_SLOW: str = 'speed_slow'
    SPEED_WEEKLY: str = 'speed_weekly'
