from typing import List, Text


class KubicCommand(object):
    def __init__(self, command: Text, *options: List[Text]):
        self.command = command
        self.options = options

    def __str__(self) -> Text:
        options_chained_by_space = ' '.join(self.options)
        return f'{self.command} {options_chained_by_space}'
