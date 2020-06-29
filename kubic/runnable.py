from abc import ABCMeta, abstractmethod
from typing import Generic, Text, TypeVar


I, O = TypeVar('I'), TypeVar('O')


class KubicRunnable(metaclass=ABCMeta):
    @abstractmethod
    def run(self, option: Generic[I]) -> Generic[O]:
        pass
