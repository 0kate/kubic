from kubic.config import KubicConfig
from kubic.repl import KubicRepl


def run():
    repl = KubicRepl()
    config = KubicConfig()

    repl.run(config)
