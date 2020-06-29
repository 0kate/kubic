from abc import ABCMeta, abstractmethod
from typing import Generic, Optional, Text, TypeVar


I, O = TypeVar('I'), TypeVar('O')


class KubicRunnable(metaclass=ABCMeta):
    @abstractmethod
    def run(self, option: Genercit[I]) -> Optional[O]:
        pass
