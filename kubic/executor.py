import subprocess
from typing import Text

from kubic.command import KubicCommand
from kubic.runnable import KubicRunnable


class KubicExecutor(KubicRunnable):
    KUBECTL = 'kubectl'

    def run(self, option: KubicCommand) -> Text:
        return ''

    def get_kubectl_config(self): 
        config = subprocess.check_output([self.__class__.KUBECTL, 'config', 'view'])
        return config
