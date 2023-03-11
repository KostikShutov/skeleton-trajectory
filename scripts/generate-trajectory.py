import math
import json
import random
from tqdm import tqdm
from components.config.Config import Config
from utils.Utils import createDirectory, parseArgs
from utils.Math import normalizeAngle


def generateTrajectory(number: int) -> list[object]:
    x: float = 0.0  # [m]
    y: float = 0.0  # [m]
    speed: float = Config.SPEED  # [m/s]
    length: float = Config.LENGTH  # [m]
    yaw: float = math.radians(0.0)  # [rad]
    steering: float = generateSteering()  # [rad]
    points: int = generatePoints()
    result: list[object] = [{
        'x': x,
        'y': y,
        'yaw': math.degrees(yaw),
        'steering': math.degrees(steering),
        'speed': speed,
    }]

    for _ in tqdm(range(number), desc='Generating trajectory'):
        for _ in range(points):
            x += speed * math.cos(yaw) * Config.GENERATE_DURATION  # [m]
            y += speed * math.sin(yaw) * Config.GENERATE_DURATION  # [m]
            yaw += math.tan(steering) * (speed / length) * Config.GENERATE_DURATION  # [rad]
            yaw: float = normalizeAngle(yaw)  # [rad]

        steering: float = generateSteering()  # [rad]
        points: int = generatePoints()

        result.append({
            'x': x,
            'y': y,
            'yaw': math.degrees(yaw),
            'steering': math.degrees(steering),
            'speed': speed,
        })

    return result


def generateSteering() -> float:
    return math.radians(float(random.randint(-45, 45)))


def generatePoints() -> int:
    return random.randint(10, 40)


def saveTrajectory(path: str, trajectory: list[object]) -> None:
    with open(path, 'w') as file:
        file.write(json.dumps(trajectory))
        file.write('\n')


def main() -> None:
    args: any = parseArgs()
    number: int = args.number
    modelDirectory: str = 'model/' + args.model + '/'
    modelFile: str = args.file

    trajectory: list[object] = generateTrajectory(number=number)
    createDirectory(directory=modelDirectory)

    saveTrajectory(
        path=modelDirectory + modelFile + '.json',
        trajectory=trajectory,
    )


if __name__ == '__main__':
    main()
