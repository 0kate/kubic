import sys

from prompt_toolkit import prompt


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
        pass

    def run(self):
        print(self.__class__.LABEL)

        while True:
            command = prompt('(kubic)\n>> ')
            if command == 'exit':
                sys.exit(0)
            print(command)
