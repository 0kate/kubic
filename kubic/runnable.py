from abc import ABCMeta, abstractmethod
from typing import Generic, Option, Text, TypeVar


I, O = TypeVar('I'), TypeVar('O')


class KubicRunnable(metaclass=ABCMeta):
    @abstractmethod
    def run(self, option: Genercit[I]) -> Option[O]:
        pass
