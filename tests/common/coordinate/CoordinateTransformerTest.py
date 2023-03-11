import unittest
from components.coordinate.Coordinate import Coordinate
from components.coordinate.CoordinateTransformer import CoordinateTransformer


class coordinateTransformerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.coordinateTransformer = CoordinateTransformer()

    def testSeparateToXYLists(self) -> None:
        actual: tuple[list[float], list[float]] = self.coordinateTransformer.separateToXYLists([])
        self.assertEqual(([], []), actual)

        actual: tuple[list[float], list[float]] = self.coordinateTransformer.separateToXYLists([
            Coordinate(x=1.2, y=3.4),
            Coordinate(x=11.12, y=13.14),
        ])
        self.assertEqual((
            [1.2, 11.12],
            [3.4, 13.14],
        ), actual)

    def testSplitInfoFragments(self) -> None:
        actual: list[list[Coordinate]] = self.coordinateTransformer.splitInfoFragments([])
        self.assertEqual([], actual)

        actual: list[list[Coordinate]] = self.coordinateTransformer.splitInfoFragments([
            Coordinate(1.2, 3.4),
        ])
        self.assertEqual([], actual)

        actual: list[list[Coordinate]] = self.coordinateTransformer.splitInfoFragments([
            Coordinate(1.2, 3.4),
            Coordinate(5.6, 7.8),
        ])
        self.assertEqual([
            [Coordinate(1.2, 3.4), Coordinate(5.6, 7.8)]
        ], actual)

        actual: list[list[Coordinate]] = self.coordinateTransformer.splitInfoFragments([
            Coordinate(1.2, 3.4),
            Coordinate(5.6, 7.8),
            Coordinate(9.10, 11.12),
        ])
        self.assertEqual([
            [Coordinate(1.2, 3.4), Coordinate(5.6, 7.8)],
            [Coordinate(5.6, 7.8), Coordinate(9.10, 11.12)]
        ], actual)

    def testAddFictionalCoordinates(self) -> None:
        actual: list[Coordinate] = self.coordinateTransformer.addFictionalCoordinates([], 3)
        self.assertEqual([], actual)

        actual: list[Coordinate] = self.coordinateTransformer.addFictionalCoordinates([
            Coordinate(x=1.2, y=3.4),
        ], 3)
        self.assertEqual([], actual)

        actual: list[Coordinate] = self.coordinateTransformer.addFictionalCoordinates([
            Coordinate(x=1.2, y=3.4),
            Coordinate(x=5.6, y=7.8),
        ], 0)
        self.assertEqual([], actual)

        actual: list[Coordinate] = self.coordinateTransformer.addFictionalCoordinates([
            Coordinate(x=1.2, y=3.4),
            Coordinate(x=5.6, y=7.8),
        ], 3)
        self.assertEqual([
            Coordinate(x=1.2, y=3.4),
            Coordinate(x=5.6, y=7.8),
            Coordinate(x=10.0, y=12.2),
            Coordinate(x=14.4, y=16.6),
            Coordinate(x=18.8, y=21.0),
        ], actual)


if __name__ == '__main__':
    unittest.main()
