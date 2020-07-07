from unittest import TestCase, mock

from kubic.config import KubicConfig
from kubic.errors import KubectlNotInstalledError
from kubic.repl import KubicRepl


class TestKubicRepl(TestCase):
    def setUp(self):
        self.repl = KubicRepl()

    def test_initialize(self):
        self.assertIsInstance(self.repl, KubicRepl)

    @mock.patch("shutil.which")
    def test_run_case_kubectl_is_not_installed(self, mock_shutil_which):
        mock_shutil_which.return_value = None
        config = KubicConfig()
        with self.assertRaises(KubectlNotInstalledError):
            self.repl.run(config)
