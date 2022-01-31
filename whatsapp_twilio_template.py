import requests
import json
import sys
import os
import hashlib
import hmac
import base64
import requests
import json
import time
import phonenumbers

twilio_SID = ""
twilio_token = ""

serviceId = ""
channelId = ""

url = ""

def getTemplateInfo():
  """Returns a list of templates which the user can choose from"""

  templateCodeArray = [] #Array of Template codes or names, if applicable

  return templateCodeArray

def getTemplateDetail():
  """Returns the details & text of a specific template"""

  response = None
  return response

def send_message(recepient_user, template_data):

  print(recepient_user.message_consent)
  if not recepient_user.phone:
    raise Exception("NO_PHONE_NUMBER")
  if not recepient_user.message_consent:
    raise Exception("NO_MESSAGE_CONSENT")

  phone = recepient_user.phone
  parsed_phone = phonenumbers.parse(phone.as_e164)
  to_country = parsed_phone.country_code
  to_number = phone.as_e164.replace("+", "")

  template = getTemplateDetail()

  return True

