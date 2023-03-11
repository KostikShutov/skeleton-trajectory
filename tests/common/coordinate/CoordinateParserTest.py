import unittest
from components.coordinate.Coordinate import Coordinate
from components.coordinate.CoordinateParser import CoordinateParser


class CoordinateParserTest(unittest.TestCase):
    def setUp(self) -> None:
        self.coordinateParser = CoordinateParser()

    def testParse(self) -> None:
        actual: list[Coordinate] = self.coordinateParser.parse([])
        self.assertEqual([], actual)

        actual: list[Coordinate] = self.coordinateParser.parse([
            {'x': 1.2, 'y': 3.4},
            {'x': 5.6, 'y': 7.8},
        ])
        self.assertEqual([
            Coordinate(x=1.2, y=3.4),
            Coordinate(x=5.6, y=7.8),
        ], actual)


if __name__ == '__main__':
    unittest.main()
