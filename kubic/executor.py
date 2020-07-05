import subprocess
from typing import Text

from kubic.command import KubicCommand
from kubic.runnable import KubicRunnable


class KubicExecutor(KubicRunnable):
    KUBECTL = 'kubectl'

    def run(self, command: KubicCommand) -> Text:
        kubectl_with_options = [self.__class__.KUBECTL]
        kubectl_with_options.extend(command.with_options)
        output = self._call_subprocess(kubectl_with_options)
        return output

    def _call_subprocess(self, commands) -> Text:
        return subprocess.check_output(commands).decode('utf-8').strip()
