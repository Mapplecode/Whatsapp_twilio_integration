# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

TWILIO_TOKEN = '2d1f78ccce58a4ae6835b40236c74674'
TWILIO_SID = 'AC7524158f2ee1ed51c9066d222d26e4db'
TWILIO_NUMBER = '+17755425226'

from twilio.rest import Client

account_sid = 'AC7524158f2ee1ed51c9066d222d26e4db'
auth_token = '2d1f78ccce58a4ae6835b40236c74674'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='Hello! This is an editable text message. You are free to change it and write whatever you like.',
    to='whatsapp:+919915333337'
)

print(message.sid)