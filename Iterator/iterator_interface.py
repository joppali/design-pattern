from abc import ABCMeta, abstractmethod

class Iterator(metaclass=ABCMeta):
    @abstractmethod
    def has_next() -> bool:
        pass
    
    @abstractmethod
    def next() -> object:
        pass 
