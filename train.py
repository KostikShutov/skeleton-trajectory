#!/usr/bin/python

from utils.Logger import Logger
from components.command.CommandTransformer import CommandTransformer
from components.coordinate.CoordinateParser import CoordinateParser
from components.coordinate.CoordinateTransformer import CoordinateTransformer
from components.part.PartTransformer import PartTransformer
from generator.TrainService import TrainService
from generator.TrainHelper import TrainHelper
from utils.Utils import parseArgs

Logger('train')


def getTrainService() -> TrainService:
    return TrainService(
        coordinateParser=CoordinateParser(),
        trainHelper=TrainHelper(
            coordinateTransformer=CoordinateTransformer(),
            commandTransformer=CommandTransformer(),
            partTransformer=PartTransformer(),
        ),
    )


def main() -> None:
    args: any = parseArgs()
    modelName: str = args.model

    getTrainService().train(modelName=modelName)


if __name__ == '__main__':
    main()
