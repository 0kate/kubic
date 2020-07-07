from typing import Text

from kubic.command import KubicCommand
from kubic.runnable import KubicRunnable


class KubicTranslator(KubicRunnable):
    """KubicTranslator."""

    def run(self, option: Text) -> KubicCommand:
        """run.

        :param option:
        :type option: Text
        :rtype: KubicCommand
        """
        command, *options = option.split(" ")
        command = KubicCommand(command, options=options)
        return command
