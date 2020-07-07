from setuptools import find_packages, setup

setup(
    name="kubic",
    version="0.1.0",
    description="kubectl interactive console",
    packages=find_packages(),
    entry_points={"console_scripts": ["kubic = kubic.kubic:run"]},
    install_requires=open("requirements.txt").read().splitlines(),
)
