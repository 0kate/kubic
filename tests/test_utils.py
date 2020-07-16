from unittest import TestCase, mock

from kubic.utils import is_command_exists, parse_table_kubectl_returned


class TestUtils(TestCase):
    @mock.patch("shutil.which")
    def test_command_is_exists(self, mock_shutil_which):
        mock_shutil_which.return_value = "/path/to/command"
        self.assertTrue(is_command_exists("valid"))

    @mock.patch("shutil.which")
    def test_command_is_not_exists(self, mock_shutil_which):
        mock_shutil_which.return_value = None
        self.assertFalse(is_command_exists("invalid"))

    def test_parse_table_kubectl_returned(self):
        TEST_DATA = (
            "NAME                              SHORTNAMES   APIGROUP                       NAMESPACED   KIND\n"
            "bindings                                                                      true         Binding\n"
            "deployments                       deploy       apps                           true         Deployment\n"
            "persistentvolumes                 pv                                          false        PersistentVolume"
        )
        header, *contents = TEST_DATA.split("\n")
        parsed_header, parsed_contents = parse_table_kubectl_returned(header, contents)
        expected_parsed_header = [
            "NAME", "SHORTNAMES", "APIGROUP", "NAMESPACED", "KIND",
        ]
        expected_parsed_contents = [
            ["bindings", "", "", "true", "Binding"],
            ["deployments", "deploy", "apps", "true", "Deployment"],
            ["persistentvolumes", "pv", "", "false", "PersistentVolume"],
        ]
        self.assertEqual(
            (parsed_header, parsed_contents),
            (expected_parsed_header, expected_parsed_contents),
        )
