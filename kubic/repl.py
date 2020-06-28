import sys

import yaml
from prompt_toolkit import prompt

from kubic.executor import KubicExecutor
from kubic.translator import KubicTranslator


class KubicRepl(object):
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
        self.current_context = self._get_current_context()

    def run(self):
        print(self.__class__.LABEL)

        while True:
            command = prompt(f'Context: [{self.current_context}]\n>> ')
            if command == 'exit':
                sys.exit(0)
            print(command)

    def _get_current_context(self):
        kubectl_config = yaml.load(self.executor.get_kubectl_config(), Loader=yaml.FullLoader)
        return kubectl_config['current-context']

