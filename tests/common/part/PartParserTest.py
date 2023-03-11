import unittest
from components.coordinate.Coordinate import Coordinate
from components.coordinate.CoordinateParser import CoordinateParser
from components.part.Part import Part
from components.part.PartParser import PartParser


class PartParserTest(unittest.TestCase):
    def setUp(self) -> None:
        self.partParser = PartParser(CoordinateParser())

    def testParse(self) -> None:
        actual: Part = self.partParser.parse({
            'coordinates': [],
            'yaw': 33.5
        })
        self.assertEqual(Part(
            coordinates=[],
            yaw=33.5,
        ), actual)

        actual: Part = self.partParser.parse({
            'coordinates': [
                {'x': 1.2, 'y': 3.4},
                {'x': 5.6, 'y': 7.8},
            ],
            'yaw': 33.5
        })
        self.assertEqual(Part(
            coordinates=[
                Coordinate(x=1.2, y=3.4),
                Coordinate(x=5.6, y=7.8),
            ],
            yaw=33.5,
        ), actual)
