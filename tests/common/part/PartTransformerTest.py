import unittest
from components.coordinate.Coordinate import Coordinate
from components.part.Part import Part
from components.part.PartTransformer import PartTransformer


class PartTransformerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.partTransformer = PartTransformer()

    def testPresentForInput(self) -> None:
        with self.assertRaises(ValueError) as context:
            self.partTransformer.presentForInput(Part(
                coordinates=[],
                yaw=44.9,
            ))

        self.assertTrue('Must provide 2 coordinates' in str(context.exception))

        with self.assertRaises(ValueError) as context:
            self.partTransformer.presentForInput(Part(
                coordinates=[Coordinate(x=1.2, y=3.4)],
                yaw=44.9,
            ))

        self.assertTrue('Must provide 2 coordinates' in str(context.exception))

        with self.assertRaises(ValueError) as context:
            self.partTransformer.presentForInput(Part(
                coordinates=[
                    Coordinate(x=1.2, y=3.4),
                    Coordinate(x=5.6, y=7.8),
                ],
                yaw=44.9,
            ))

        self.assertTrue('First y coordinate must be 0' in str(context.exception))

        with self.assertRaises(ValueError) as context:
            self.partTransformer.presentForInput(Part(
                coordinates=[
                    Coordinate(x=1.2, y=0.0),
                    Coordinate(x=5.6, y=7.8),
                    Coordinate(x=9.10, y=11.12),
                ],
                yaw=13.14,
            ))

        self.assertTrue('Must provide 2 coordinates' in str(context.exception))

        actual: list[float] = self.partTransformer.presentForInput(Part(
            coordinates=[
                Coordinate(x=1.2, y=0.0),
                Coordinate(x=5.6, y=7.8),
            ],
            yaw=9.10,
        ))
        self.assertEqual([1.2, 8.9554452709, 60.5725435968, 9.10], actual)

    def testNormalizeToZero(self) -> None:
        with self.assertRaises(ValueError):
            self.partTransformer.normalizeToZero(Part(
                coordinates=[],
                yaw=85.5,
            ))

        with self.assertRaises(ValueError):
            self.partTransformer.normalizeToZero(Part(
                coordinates=[Coordinate(x=1.2, y=3.4)],
                yaw=85.5,
            ))

        actual: Part = self.partTransformer.normalizeToZero(Part(
            coordinates=[
                Coordinate(x=1.2, y=3.4),
                Coordinate(x=5.6, y=10.8),
                Coordinate(x=9.10, y=15.12),
            ],
            yaw=96.6,
        ))
        self.assertEqual(Part(
            coordinates=[
                Coordinate(x=8.6092973, y=0.0),
                Coordinate(x=14.1112562113, y=-0.8005299108)
            ],
            yaw=37.3354877019,
        ), actual)

        actual: Part = self.partTransformer.normalizeToZero(Part(
            coordinates=[
                Coordinate(x=1.2, y=3.4),
                Coordinate(x=5.6, y=10.8),
                Coordinate(x=9.10, y=15.12),
            ],
            yaw=-178.4,
        ))
        self.assertEqual(Part(
            coordinates=[
                Coordinate(x=8.6092973, y=0.0),
                Coordinate(x=14.1112562113, y=-0.8005299108)
            ],
            yaw=122.3354877019,
        ), actual)
