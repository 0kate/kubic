from unittest import TestCase

from kubic.command import KubicCommand


class TestKubicCommand(TestCase):
    def setUp(self):
        self.command = KubicCommand('get', options=['pod'])

    def test_str(self):
        self.assertEqual(str(self.command), 'get pod')

    def test_get_property_of_with_options(self):
        self.assertEqual(self.command.with_options, ['get', 'pod'])
