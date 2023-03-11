from components.coordinate.CoordinateParser import CoordinateParser
from components.part.Part import Part


class PartParser:
    def __init__(self, coordinateParser: CoordinateParser) -> None:
        self.coordinateParser = coordinateParser

    def parse(self, data: object) -> Part:
        return Part(
            coordinates=self.coordinateParser.parse(data['coordinates']),
            yaw=float(data['yaw']),
        )
