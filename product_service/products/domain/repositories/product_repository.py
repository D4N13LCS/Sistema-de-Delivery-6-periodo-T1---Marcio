from abc import ABC, abstractmethod

class ProductRepository(ABC):

    @abstractmethod
    def list_all(self):
        pass