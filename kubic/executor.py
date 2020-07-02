import subprocess
from typing import Text

from kubic.command import KubicCommand
from kubic.runnable import KubicRunnable


class KubicExecutor(KubicRunnable):
    KUBECTL = 'kubectl'

    def run(self, command: KubicCommand) -> Text:
        kubectl_with_options = [self.__class__.KUBECTL]
        kubectl_with_options.extend(command.with_options)
        output = subprocess.check_output(kubectl_with_options).decode('utf-8')
        return output.strip()

    def get_kubectl_config(self):
        config = subprocess.check_output([self.__class__.KUBECTL, 'config', 'view'])
        return config
