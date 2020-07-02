from typing import Text
from unittest import TestCase

from kubic.command import KubicCommand
from kubic.executor import KubicExecutor


class TestKubicExecutor(TestCase):
    TEST_DATA = KubicCommand('get', 'pod')

    def setUp(self):
        executor = KubicExecutor()
        self.executor_returned = executor.run(self.__class__.TEST_DATA)

    def test_run_and_return_text(self):
        self.assertIsInstance(self.executor_returned, Text)
