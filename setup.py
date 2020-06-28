from setuptools import setup


setup(
    name='kubic',
    version='0.1.0',
    description='kubectl interactive console',
    entry_points={
        'console_scripts': [
            'kubic = kubic.kubic:main',
        ]
    }
)
