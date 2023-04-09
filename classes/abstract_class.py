from abc import ABC, abstractmethod


class Servises(ABC):

    @abstractmethod
    def get_data(self):
        pass
