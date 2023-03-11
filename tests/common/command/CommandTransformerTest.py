import unittest
from components.command.Command import Command
from components.command.CommandTransformer import CommandTransformer


class CommandTransformerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.commandTransformer = CommandTransformer()

    def testPresentForOutput(self) -> None:
        actual: list[float] = self.commandTransformer.presentForOutput(
            Command(steering=1.2, speed=3.4),
        )
        self.assertEqual([1.2, 3.4], actual)


if __name__ == '__main__':
    unittest.main()
