import subprocess
from typing import Text

from kubic.command import KubicCommand
from kubic.errors import CommandNotFoundError
from kubic.output import KubicOutput
from kubic.runnable import KubicRunnable
from kubic.utils import is_command_exists


class KubicExecutor(KubicRunnable):
    """KubicExecutor."""

    KUBECTL = "kubectl"

    def run(self, command: KubicCommand) -> KubicOutput:
        """run.

        :param command:
        :type command: KubicCommand
        :rtype: KubicOutput
        """
        kubectl_with_options = [self.__class__.KUBECTL]
        kubectl_with_options.extend(command.with_options)
        try:
            output = self._call_subprocess(kubectl_with_options)
        except subprocess.CalledProcessError:
            if is_command_exists(command.command):
                try:
                    output = self._call_subprocess(command.with_options)
                except subprocess.CalledProcessError:
                    raise CommandNotFoundError()
            else:
                raise CommandNotFoundError()
        return output

    def _call_subprocess(self, commands) -> KubicOutput:
        """_call_subprocess.

        :param commands:
        :rtype: KubicOutput
        """
        output = KubicOutput()
        output.text = (
            subprocess.check_output(commands, stderr=subprocess.STDOUT)
            .decode("utf-8")
            .strip()
        )
        return output
