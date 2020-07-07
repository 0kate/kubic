from typing import Text
from unittest import TestCase

from kubic.command import KubicCommand
from kubic.errors import CommandNotFoundError
from kubic.executor import KubicExecutor


class TestKubicExecutor(TestCase):
    def setUp(self):
        self.executor = KubicExecutor()

    def test_invalid_command(self):
        command = KubicCommand("invalid", ["command"])
        with self.assertRaises(CommandNotFoundError):
            self.executor.run(command)
