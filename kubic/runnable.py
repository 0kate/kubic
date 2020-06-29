from abc import ABCMeta, abstractmethod
from typing import Generic, Option, Text, TypeVar


T = TypeVar('T')


class KubicRunnable(metaclass=ABCMeta):
    @abstractmethod
    def run(self, option: Genercit[T]) -> Option[Text]:
        pass
