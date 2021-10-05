import os
import requests

pixela_ep = 'https://pixe.la/v1/users'

user_params = {
    'token': os.environ.get('PIXELA_TOKEN'),
    'username': 'benwade',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

response = requests.post(pixela_ep, json=user_params)
print(response.text)