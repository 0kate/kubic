from unittest import TestCase, mock

from kubic.command import KubicCommand
from kubic.errors import CommandNotFoundError
from kubic.executor import KubicExecutor
from kubic.output import KubicOutput


class TestKubicExecutor(TestCase):
    def setUp(self):
        self.executor = KubicExecutor()

    @mock.patch("subprocess.check_output")
    def test_run_and_return_kubic_output(self, mock_check_output):
        mock_check_output.return_value = b"output\n"
        command = KubicCommand("command", [])
        output = self.executor.run(command)
        self.assertIsInstance(output, KubicOutput)

    def test_invalid_command(self):
        command = KubicCommand("invalid", ["command"])
        with self.assertRaises(CommandNotFoundError):
            self.executor.run(command)
