import sys

from kubic.config import KubicConfig
from kubic.errors import KubectlNotInstalledError
from kubic.repl import KubicRepl


def run():
    """run."""
    repl = KubicRepl()
    config = KubicConfig()

    try:
        repl.run(config)
    except KubectlNotInstalledError:
        print("Error: kubectl is not installed.")
        sys.exit(0)
