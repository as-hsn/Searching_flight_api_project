import smtplib
from twilio.rest import Client

TWILIO_SID = 'ACf37e9ba82b2a1fa04850938939bc9905'
TWILIO_AUTH_TOKEN ='2be470c103c400f2df773a50f6a6ebc9'
TWILIO_VIRTUAL_NUMBER = '+12247570446'
TWILIO_VERIFIED_NUMBER = 'Sender Number'
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL ="Your Email"
MY_PASSWORD = "Email password"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )