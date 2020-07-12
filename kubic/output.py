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
        print(f"{self.text}\n")

    def _print_other_output(self):
        """_print_other_output."""
        print(f"{self.text}\n")
