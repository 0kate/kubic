from rich import syntax as rich_syntax
from rich import table as rich_table

from kubic.utils import parse_table_kubectl_returned


class KubicOutput(object):
    """KubicOutput."""

    def styling(self):
        """styling."""
        styling_method_name = f"_styling_{self.kind}"

        if hasattr(self, styling_method_name):
            styling_method = getattr(self, styling_method_name)
        else:
            styling_method = getattr(self, "_styling_other")

        return styling_method()

    def _styling_get(self):
        """_styling_get."""
        RESOURCE_NOT_FOUND_KEYWORD = "No resources"

        if self.text.startswith(RESOURCE_NOT_FOUND_KEYWORD):
            output_contents = self.text
            options = {
                "style": "bold red",
            }
        else:
            table = rich_table.Table(show_header=True, header_style="bold magenta")

            header_row, *item_rows = self.text.split("\n")
            header, items = parse_table_kubectl_returned(header_row, item_rows)

            for col in header:
                table.add_column(col)

            for item in items:
                table.add_row(*item)

            output_contents = table
            options = {}

        return output_contents, options

    def _styling_describe(self):
        """_styling_describe_output."""
        syntax = rich_syntax.Syntax(self.text, "yaml", line_numbers=True)
        return syntax, {}

    def _styling_other(self):
        """_print_other_output."""
        return self.text, {}
