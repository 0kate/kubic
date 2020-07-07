import sys
from typing import Text

from prompt_toolkit import prompt

from kubic.command import KubicCommand
from kubic.config import KubicConfig
from kubic.executor import KubicExecutor
from kubic.runnable import KubicRunnable
from kubic.translator import KubicTranslator


class KubicRepl(KubicRunnable):
    """KubicRepl."""

    LABEL = """
         ___           ___                                     ___     
        /__/|         /__/\         _____        ___          /  /\    
       |  |:|         \  \:\       /  /::\      /  /\        /  /:/    
       |  |:|          \  \:\     /  /:/\:\    /  /:/       /  /:/     
     __|  |:|      ___  \  \:\   /  /:/~/::\  /__/::\      /  /:/  ___ 
    /__/\_|:|____ /__/\  \__\:\ /__/:/ /:/\:| \__\/\:\__  /__/:/  /  /\\
    \  \:\/:::::/ \  \:\ /  /:/ \  \:\/:/~/:/    \  \:\/\ \  \:\ /  /:/
     \  \::/~~~~   \  \:\  /:/   \  \::/ /:/      \__\::/  \  \:\  /:/ 
      \  \:\        \  \:\/:/     \  \:\/:/       /__/:/    \  \:\/:/  
       \  \:\        \  \::/       \  \::/        \__\/      \  \::/   
        \__\/         \__\/         \__\/                     \__\/    
    """

    def __init__(self):
        """__init__."""
        self.executor = KubicExecutor()
        self.translator = KubicTranslator()

    def run(self, config: KubicConfig) -> None:
        """run.

        :param config:
        :type config: KubicConfig
        :rtype: None
        """
        print(self.__class__.LABEL)

        while True:
            current_context = self._get_current_context()
            user_input = prompt(f"Context: [{current_context}]\n>> ")
            if user_input in ("exit", "quit"):
                sys.exit(0)
            command = self._translate(user_input)
            output = self._dispatch(command)
            print(f"{output}\n")

    def _dispatch(self, command: KubicCommand) -> Text:
        """_dispatch.

        :param command:
        :type command: KubicCommand
        :rtype: Text
        """
        return self.executor.run(command)

    def _translate(self, user_input: Text) -> KubicCommand:
        """_translate.

        :param user_input:
        :type user_input: Text
        :rtype: KubicCommand
        """
        return self.translator.run(user_input)

    def _get_current_context(self) -> Text:
        """_get_current_context.

        :rtype: Text
        """
        get_current_context_command = self._translate("config current-context")
        return self._dispatch(get_current_context_command)
