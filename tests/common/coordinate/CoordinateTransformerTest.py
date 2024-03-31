import unittest
from components.coordinate.Coordinate import Coordinate
from components.coordinate.CoordinateTransformer import CoordinateTransformer


class coordinateTransformerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.coordinateTransformer = CoordinateTransformer()

    def testSplitInfoFragments(self) -> None:
        actual: list[list[Coordinate]] = self.coordinateTransformer.splitInfoFragments([])
        self.assertEqual([], actual)

        actual: list[list[Coordinate]] = self.coordinateTransformer.splitInfoFragments([
            Coordinate(x=1.2, y=3.4),
        ])
        self.assertEqual([], actual)

        actual: list[list[Coordinate]] = self.coordinateTransformer.splitInfoFragments([
            Coordinate(x=1.2, y=3.4),
            Coordinate(x=5.6, y=7.8),
        ])
        self.assertEqual([], actual)

        actual: list[list[Coordinate]] = self.coordinateTransformer.splitInfoFragments([
            Coordinate(x=1.2, y=3.4),
            Coordinate(x=5.6, y=7.8),
            Coordinate(x=9.10, y=11.12),
        ])
        self.assertEqual([
            [Coordinate(x=1.2, y=3.4), Coordinate(x=5.6, y=7.8), Coordinate(x=9.10, y=11.12)],
        ], actual)

        actual: list[list[Coordinate]] = self.coordinateTransformer.splitInfoFragments([
            Coordinate(x=1.2, y=3.4),
            Coordinate(x=5.6, y=7.8),
            Coordinate(x=9.10, y=11.12),
            Coordinate(x=13.14, y=15.16),
        ])
        self.assertEqual([
            [Coordinate(x=1.2, y=3.4), Coordinate(x=5.6, y=7.8), Coordinate(x=9.10, y=11.12)],
            [Coordinate(x=5.6, y=7.8), Coordinate(x=9.10, y=11.12), Coordinate(x=13.14, y=15.16)],
        ], actual)

    def testAddFictionalCoordinate(self) -> None:
        actual: list[Coordinate] = self.coordinateTransformer.addFictionalCoordinate([])
        self.assertEqual([], actual)

        actual: list[Coordinate] = self.coordinateTransformer.addFictionalCoordinate([
            Coordinate(x=1.2, y=3.4),
        ])
        self.assertEqual([], actual)

        actual: list[Coordinate] = self.coordinateTransformer.addFictionalCoordinate([
            Coordinate(x=1.2, y=3.4),
            Coordinate(x=5.6, y=7.8),
        ])
        self.assertEqual([
            Coordinate(x=1.2, y=3.4),
            Coordinate(x=5.6, y=7.8),
            Coordinate(x=10.0, y=12.2),
        ], actual)


if __name__ == '__main__':
    unittest.main()
