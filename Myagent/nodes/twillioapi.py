from os import getenv
from dotenv import load_dotenv
load_dotenv()
from twilio.rest import Client
import json
account_sid = getenv("account_sid")
auth_token = getenv("auth_token")

client = Client(account_sid, auth_token)
message = client.messages.create(
  from_='whatsapp:+14155238886',
  content_sid='HXb5b62575e6e4ff6129ad7c8efe1f983e',
  content_variables='{"1":"anant","2":"12345"}',
  to='whatsapp:+919896493112'
)
print(message.sid,"this is message body",message.body)
