from unittest import TestCase

from kubic.output import KubicOutput
from rich import table as rich_table
from rich import syntax as rich_syntax


class TestKubicOutput(TestCase):
    def test_styling_get(self):
        TEST_DATA = (
            "NAME                              SHORTNAMES   APIGROUP                       NAMESPACED   KIND\n"
            "bindings                                                                      true         Binding"
        )
        output = KubicOutput()
        output.kind = "get"
        output.text = TEST_DATA
        styled_output, _ = output.styling()
        self.assertIsInstance(styled_output, rich_table.Table)

    def test_styling_describe(self):
        TEST_DATA = (
            "Name:         test-pod\n"
            "Namespace:    default\n"
            "Priority:     0"
        )
        output = KubicOutput()
        output.kind = "describe"
        output.text = TEST_DATA
        styled_output, _ = output.styling()
        self.assertIsInstance(styled_output, rich_syntax.Syntax)
