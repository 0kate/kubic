from typing import Text
from unittest import TestCase

from kubic.command import KubicCommand
from kubic.executor import KubicExecutor


class TestKubicExecutor(TestCase):
    TEST_DATA = KubicCommand("get", "pod")
