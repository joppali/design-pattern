from abc import ABCMeta, abstractmethod
from iterator_interface import Iterator

class Aggregate(metaclass=ABCMeta):
    @abstractmethod
    def iterator() -> Iterator:
        # return iterator class
        pass