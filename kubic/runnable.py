from abc import ABCMeta, abstractmethod
from typing import Generic, Text, TypeVar

I, O = TypeVar("I"), TypeVar("O")


class KubicRunnable(metaclass=ABCMeta):
    """KubicRunnable."""

    @abstractmethod
    def run(self, option: Generic[I]) -> Generic[O]:
        """run.

        :param option:
        :type option: Generic[I]
        :rtype: Generic[O]
        """
        pass
