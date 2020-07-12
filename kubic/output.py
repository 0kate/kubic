import rich
from rich import table as rich_table


class KubicOutput(object):
    """KubicOutput."""

    def print(self):
        """print."""
        print_method_name = f"_print_{self.kind}_output"

        if hasattr(self, print_method_name):
            print_method = getattr(self, print_method_name)
        else:
            print_method = getattr(self, "_print_other_output")

        print_method()

    def _print_get_output(self):
        """_print_get_output."""
        # print(f"{self.text}\n")
        table = rich_table.Table(show_header=True, header_style="bold magenta")

        header, *items = self.text.split("\n")

        for col in header.split():
            table.add_column(col)

        for item in items:
            row = item.split()
            table.add_row(*row)

        rich.print(table)

    def _print_other_output(self):
        """_print_other_output."""
        print(f"{self.text}\n")
