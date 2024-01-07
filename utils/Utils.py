import os
import argparse
from components.model.ModelName import ModelName


def createDirectory(directory: str) -> None:
    if not os.path.exists(directory):
        os.makedirs(directory)


def removeFirst(items: list) -> list:
    if not items:
        return []

    items = items.copy()
    items.pop(0)

    return items


def strToBool(value: str) -> bool:
    return value.lower() in ['true', '1']


def parseArgs() -> any:
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--model', type=str, default=ModelName.NORMAL)
    parser.add_argument('-f', '--file', type=str, default='train')
    parser.add_argument('-n', '--number', type=int, default=1_000_000)
    parser.add_argument('-s', '--side', type=int, default=1)
    parser.add_argument('-p', '--points', type=int, default=2)

    return parser.parse_args()
