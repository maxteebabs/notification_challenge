from notifications.abstractions.SMSProvider import SMSProvider

class SMSService:
    def __init__(self, provider: SMSProvider):
        self.provider = provider

    def send(self, message, mobile):
        return self.provider.sendSMS(message, mobile)