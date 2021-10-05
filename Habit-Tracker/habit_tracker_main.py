import os
import requests
import datetime

pixela_ep = 'https://pixe.la/v1/users'

user_params = {
    'token': os.environ.get('PIXELA_TOKEN'),
    'username': 'benwade',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(pixela_ep, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_ep}/benwade/graphs"
graph_params = {
    'id': 'graph1',
    'name': 'Reassignment',
    'unit': 'hours',
    'type': 'float',
    'color': 'shibafu'
}
header = {
    'X-USER-TOKEN': os.environ.get('PIXELA_TOKEN')
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=header)
# print(response.text)
today = datetime.datetime.now().strftime('%Y%m%d')
pixel_ep = f"{pixela_ep}/benwade/graphs/graph1"
pixel_params = {
    'date': today,
    'quantity': '6.5',
    'optionalData': "{\"Route\": \"900\"}"
}

response = requests.post(url=pixel_ep, json=pixel_params, headers=header)
print(response.text)
