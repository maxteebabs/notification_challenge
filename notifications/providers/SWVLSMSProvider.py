from flask import current_app
import os
from notifications.abstractions.SMSProvider import SMSProvider
import requests

class SWVLSMSProvider(SMSProvider):
    def sendSMS(self, message, mobile):
        """Overriddes the SMSProvider. Send SMS using this provider"""
        url = os.environ.get("SMS_BASE_URL")
        current_app.logger.info('%s swvlsmsprovider', url)
        return True