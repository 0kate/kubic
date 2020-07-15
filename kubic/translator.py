from typing import Text

from kubic.command import KubicCommand
from kubic.runnable import KubicRunnable


class KubicTranslator(KubicRunnable):
    """KubicTranslator."""
    def __init__(self):
        """__init__."""
        self.resources_set = set()

    def run(self, option: Text) -> KubicCommand:
        """run.

        :param option:
        :type option: Text
        :rtype: KubicCommand
        """
        command, *options = option.split(" ")
        if command in self.resources_set:
            options.insert(0, command)
            command = "get"

        command = KubicCommand(command, options=options)
        return command
