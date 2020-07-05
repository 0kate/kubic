import sys
from typing import Text

from prompt_toolkit import prompt

from kubic.command import KubicCommand
from kubic.config import KubicConfig
from kubic.executor import KubicExecutor
from kubic.runnable import KubicRunnable
from kubic.translator import KubicTranslator


class KubicRepl(KubicRunnable):
    LABEL = '''
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
    '''

    def __init__(self):
        self.executor = KubicExecutor()

    def run(self, config: KubicConfig) -> None:
        print(self.__class__.LABEL)

        while True:
            current_context = self._get_current_context()
            command = prompt(f'Context: [{current_context}]\n>> ')
            if command == 'exit':
                sys.exit(0)
            print(command)

    def _dispatch(self, command: KubicCommand) -> Text:
        return self.executor.run(command)

    def _get_current_context(self) -> Text:
        get_current_context_command = \
            KubicCommand('config', 'current-context')
        return self._dispatch(get_current_context_command)
