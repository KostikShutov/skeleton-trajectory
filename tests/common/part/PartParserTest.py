import unittest
from components.coordinate.Coordinate import Coordinate
from components.coordinate.CoordinateParser import CoordinateParser
from components.part.Part import Part
from components.part.PartParser import PartParser


class PartParserTest(unittest.TestCase):
    def setUp(self) -> None:
        self.partParser = PartParser(
            coordinateParser=CoordinateParser(),
        )

    def testParse(self) -> None:
        actualPart, actualModelName = self.partParser.parse({
            'coordinates': [],
            'yaw': 33.5,
        })
        self.assertEqual(Part(
            coordinates=[],
            yaw=33.5,
        ), actualPart)
        self.assertEqual('static_smoothly', actualModelName)

        actualPart, actualModelName = self.partParser.parse({
            'coordinates': [
                {'x': 1.2, 'y': 3.4},
                {'x': 5.6, 'y': 7.8},
            ],
            'yaw': 33.5,
            'model': 'static_aggressive',
        })
        self.assertEqual(Part(
            coordinates=[
                Coordinate(x=1.2, y=3.4),
                Coordinate(x=5.6, y=7.8),
            ],
            yaw=33.5,
        ), actualPart)
        self.assertEqual('static_aggressive', actualModelName)
