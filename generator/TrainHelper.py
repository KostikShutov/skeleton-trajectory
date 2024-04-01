from tqdm import tqdm
from components.command.Command import Command
from components.command.CommandTransformer import CommandTransformer
from components.coordinate.Coordinate import Coordinate
from components.coordinate.CoordinateTransformer import CoordinateTransformer
from components.coordinate.State import State
from components.part.Part import Part
from components.part.PartTransformer import PartTransformer


class TrainHelper:
    def __init__(self, coordinateTransformer: CoordinateTransformer,
                 commandTransformer: CommandTransformer,
                 partTransformer: PartTransformer) -> None:
        self.coordinateTransformer = coordinateTransformer
        self.commandTransformer = commandTransformer
        self.partTransformer = partTransformer

    def createItems(self, course: list[Coordinate]) -> list[tuple[Part, Command]]:
        result: list[tuple[Part, Command]] = []
        fragments: list[list[Coordinate]] = self.coordinateTransformer.splitInfoFragments(coordinates=course)

        for fragment in tqdm(fragments, desc='Creating training items'):
            state: State = fragment[0].state

            if state is None:
                raise ValueError('State can not be "None"')

            part: Part = self.partTransformer.normalizeToZero(Part(
                coordinates=fragment,
                yaw=state.yaw,
            ))

            command: Command = Command(
                steering=state.steering,
                speed=state.speed,
            )

            result.append((part, command))

        return result

    def presentItems(self, items: list) -> tuple[list[list[float]], list[list[float]], list[list[float]]]:
        trainX: list[list[float]] = []
        trainSteeringY: list[list[float]] = []
        trainSpeedY: list[list[float]] = []

        for part, command in tqdm(items, desc='Presenting training items'):
            trainX.append(self.partTransformer.presentForInput(part))
            trainSteeringY.append([command.steering])
            trainSpeedY.append([command.speed])

        return trainX, trainSteeringY, trainSpeedY
