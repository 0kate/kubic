import shutil
from typing import Text


def is_command_exists(command: Text):
    """is_command_exists.

    :param command:
    :type command: Text
    """
    return shutil.which(command) is not None
