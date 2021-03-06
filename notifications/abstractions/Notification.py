from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def notify():
        """This method will be overridden"""
        pass