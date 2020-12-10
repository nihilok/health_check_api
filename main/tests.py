import json
import requests

from django.test import TestCase



def check_api():
    url = "https://sandbox.api.service.nhs.uk/oauth2?secret=Oo0rID4WHBbqBBk0"
    data = json.loads(requests.post(url).content.decode())
    print(data)

check_api()

api_key = 'DLXmBirmAtYdxt9WURax2ADt3IHCDOj5'
secret = 'Oo0rID4WHBbqBBk0'