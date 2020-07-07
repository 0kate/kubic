from typing import List, Text


class KubicCommand(object):
    """KubicCommand."""

    def __init__(self, command: Text, options: List[Text] = []):
        """__init__.

        :param command:
        :type command: Text
        :param options:
        :type options: List[Text]
        """
        self.command = command
        self.options = options

    def __str__(self) -> Text:
        """__str__.

        :rtype: Text
        """
        options_chained_by_space = " ".join(self.options)
        return f"{self.command} {options_chained_by_space}"

    @property
    def with_options(self) -> List[Text]:
        """with_options.

        :rtype: List[Text]
        """
        return [self.command] + self.options
