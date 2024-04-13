from components.coordinate.CoordinateParser import CoordinateParser
from components.part.Part import Part
from components.model.ModelName import ModelName


class PartParser:
    def __init__(self, coordinateParser: CoordinateParser) -> None:
        self.coordinateParser = coordinateParser

    def parse(self, data: object) -> tuple[Part, str]:
        part: Part = Part(
            coordinates=self.coordinateParser.parse(data['coordinates']),
            yaw=float(data['yaw']),
        )

        modelName: ModelName = ModelName(str(data['model'])) if 'model' in data else ModelName.STATIC_SMOOTHLY

        return part, modelName.value
