from unittest import TestCase

from kubic.command import KubicCommand


class TestKubicCommand(TestCase):
    def setUp(self):
        self.command = KubicCommand('get', 'pod')

    def test_str(self):
        self.assertEqual(str(self.command), 'get pod')
