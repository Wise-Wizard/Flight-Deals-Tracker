from twilio.rest import Client
from dotenv import load_dotenv
import os
load_dotenv(".env")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_SID = "AC04697766eb497dd5a9b3d405ac874a63"
TWILIO_VIRTUAL_NUMBER = "+17069819153"
TWILIO_VERIFIED_NUMBER = "+917406320038"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)