from abc import ABC, abstractmethod

class SMSProvider(ABC):
    # @abc.abstractproperty 
    @abstractmethod
    def sendSMS(self):
        """This method will be overridden by the implementing class"""
        pass