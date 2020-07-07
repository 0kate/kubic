from unittest import TestCase, mock

from kubic.utils import is_command_exists


class TestUtils(TestCase):
    @mock.patch("shutil.which")
    def test_command_is_exists(self, mock_shutil_which):
        mock_shutil_which.return_value = "/path/to/command"
        self.assertTrue(is_command_exists("valid"))

    @mock.patch("shutil.which")
    def test_command_is_not_exists(self, mock_shutil_which):
        mock_shutil_which.return_value = None
        self.assertFalse(is_command_exists("invalid"))
