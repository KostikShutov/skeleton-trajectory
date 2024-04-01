import math
import unittest
from components.coordinate.Coordinate import Coordinate
from helpers.Math import distanceBetweenPoints, angleBetweenVectorAndX, rotatePoints, normalizeAngle


class MathTest(unittest.TestCase):
    def testDistanceBetweenPoints(self) -> None:
        actual: float = distanceBetweenPoints([])
        self.assertEqual(0.0, actual)

        actual: float = distanceBetweenPoints([
            Coordinate(x=0, y=0),
        ])
        self.assertEqual(0.0, actual)

        actual: float = distanceBetweenPoints([
            Coordinate(x=0, y=0),
            Coordinate(x=1, y=0),
        ])
        self.assertEqual(1.0, actual)

        actual: float = distanceBetweenPoints([
            Coordinate(x=0, y=0),
            Coordinate(x=1, y=0),
            Coordinate(x=2, y=2),
        ])
        self.assertEqual(3.23606797749979, actual)

    def testAngleBetweenVectorAndX(self) -> None:
        actual: float = angleBetweenVectorAndX(
            first=Coordinate(x=5, y=6),
            second=Coordinate(x=7, y=8),
        )
        self.assertEqual(0.7853981633974483, actual)

    def testRotatePoints(self) -> None:
        with self.assertRaises(ValueError):
            rotatePoints([])

        with self.assertRaises(ValueError):
            rotatePoints([
                Coordinate(x=0, y=0),
            ])

        with self.assertRaises(ValueError):
            rotatePoints([
                Coordinate(x=4, y=3),
                Coordinate(x=5, y=5),
            ])

        actualCoordinates, actualAngle = rotatePoints([
            Coordinate(x=0, y=0),
            Coordinate(x=0, y=1),
        ])
        self.assertEqual([
            Coordinate(x=0, y=0),
            Coordinate(x=1, y=0),
        ], actualCoordinates)
        self.assertEqual(-90, actualAngle)

        actualCoordinates, actualAngle = rotatePoints([
            Coordinate(x=0, y=0),
            Coordinate(x=0, y=10),
            Coordinate(x=-10, y=10),
        ])
        self.assertEqual([
            Coordinate(x=0, y=0),
            Coordinate(x=10, y=0),
            Coordinate(x=10, y=10),
        ], actualCoordinates)
        self.assertEqual(-90, actualAngle)

        actualCoordinates, actualAngle = rotatePoints([
            Coordinate(x=0, y=0),
            Coordinate(x=0, y=-10),
            Coordinate(x=-10, y=-10),
        ])
        self.assertEqual([
            Coordinate(x=0, y=0),
            Coordinate(x=10, y=0),
            Coordinate(x=10, y=-10),
        ], actualCoordinates)
        self.assertEqual(90, actualAngle)

        actualCoordinates, actualAngle = rotatePoints([
            Coordinate(x=0, y=0),
            Coordinate(x=5.6, y=10.8),
            Coordinate(x=9.10, y=15.12),
        ])
        self.assertEqual([
            Coordinate(x=0, y=0),
            Coordinate(x=12.1655250606, y=0.0),
            Coordinate(x=17.611734712, y=-1.1185707096),
        ], actualCoordinates)
        self.assertEqual(-62.592424562181606, actualAngle)

        actualCoordinates, actualAngle = rotatePoints([
            Coordinate(x=0, y=0),
            Coordinate(x=-5, y=0),
            Coordinate(x=-10, y=0),
        ])
        self.assertEqual([
            Coordinate(x=0, y=0),
            Coordinate(x=5, y=0),
            Coordinate(x=10, y=0),
        ], actualCoordinates)
        self.assertEqual(-180, actualAngle)

    def testNormalizeAngle(self) -> None:
        actual: float = normalizeAngle(math.radians(-190))
        self.assertEqual(2.96705972839036, actual)

        actual: float = normalizeAngle(math.radians(-80))
        self.assertEqual(-1.3962634015954636, actual)

        actual: float = normalizeAngle(math.radians(0))
        self.assertEqual(0, actual)

        actual: float = normalizeAngle(math.radians(200))
        self.assertEqual(-2.792526803190927, actual)


if __name__ == '__main__':
    unittest.main()
