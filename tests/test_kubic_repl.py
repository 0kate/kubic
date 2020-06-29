from unittest import TestCase

from kubic.repl import KubicRepl


class TestKubicRepl(TestCase):
    def test_initialize(self):
        repl = KubicRepl()
        self.assertIsInstance(repl, KubicRepl)
