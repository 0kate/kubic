import sys

from prompt_toolkit import prompt


class KubicRepl(object):
    def __init__(self):
        pass

    def run(self):
        while True:
            command = prompt('(kubic)\n>> ')
            if command == 'exit':
                sys.exit(0)
            print(command)
