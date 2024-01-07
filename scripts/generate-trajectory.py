import math
import json
import random
from tqdm import tqdm
from components.config.Config import Config
from components.model.ModelName import ModelName
from utils.Utils import createDirectory, parseArgs
from utils.Math import normalizeAngle


def generateTrajectory(modelName: str, number: int) -> list[object]:
    x: float = 0.0  # [m]
    y: float = 0.0  # [m]
    speed: float = Config.SPEED  # [m/s]
    length: float = Config.LENGTH  # [m]
    yaw: float = math.radians(0.0)  # [rad]
    steering: float = generateSteering(modelName=modelName)  # [rad]
    points: int = generatePoints(modelName=modelName)
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

        x, y = modifyCoordinate(modelName=modelName, x=x, y=y, speed=speed, yaw=yaw)
        steering: float = generateSteering(modelName=modelName)  # [rad]
        points: int = generatePoints(modelName=modelName)

        result.append({
            'x': x,
            'y': y,
            'yaw': math.degrees(yaw),
            'steering': math.degrees(steering),
            'speed': speed,
        })

    return result


def modifyCoordinate(modelName: str, x: float, y: float, speed: float, yaw: float) -> tuple[float, float]:
    if modelName == ModelName.NORMAL.value:
        return x, y

    if modelName == ModelName.AGGRESSIVE.value:
        for _ in range(random.randint(10, 20)):
            x += speed * math.cos(yaw) * Config.GENERATE_DURATION  # [m]
            y += speed * math.sin(yaw) * Config.GENERATE_DURATION  # [m]

        return x, y

    raise NotImplementedError('Model not implemented')


def generateSteering(modelName: str) -> float:
    if modelName == ModelName.NORMAL.value:
        return math.radians(float(random.randint(-45, 45)))

    if modelName == ModelName.AGGRESSIVE.value:
        return math.radians(random.choice([
            float(random.randint(-45, -35)),
            float(random.randint(35, 45)),
        ]))

    raise NotImplementedError('Model not implemented')


def generatePoints(modelName: str) -> int:
    if modelName == ModelName.NORMAL.value:
        return random.randint(10, 40)

    if modelName == ModelName.AGGRESSIVE.value:
        return random.randint(10, 20)

    raise NotImplementedError('Model not implemented')


def saveTrajectory(path: str, trajectory: list[object]) -> None:
    with open(path, 'w') as file:
        file.write(json.dumps(trajectory))
        file.write('\n')


def main() -> None:
    args: any = parseArgs()
    number: int = args.number
    modelName: str = args.model
    modelDirectory: str = 'model/' + modelName + '/'
    modelFile: str = args.file

    trajectory: list[object] = generateTrajectory(modelName=modelName, number=number)
    createDirectory(directory=modelDirectory)

    saveTrajectory(
        path=modelDirectory + modelFile + '.json',
        trajectory=trajectory,
    )


if __name__ == '__main__':
    main()
