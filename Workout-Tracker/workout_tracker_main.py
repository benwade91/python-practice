import os
import requests
from datetime import datetime

nutritionix_ep = 'https://trackapi.nutritionix.com/v2/natural/exercise'

nutritionix_header = {
    'x-app-id': os.environ.get('NUTRITION-X-APP-ID'),
    'x-app-key': os.environ.get('NUTRITION-API-KEY')
}

workout = input("What was your workout today?")

user_info = {
 "query": workout,
 "gender": "Male",
 "weight_kg": 72.5,
 "height_cm": 167.64,
 "age": 30
}

response = requests.post(url=nutritionix_ep, json=user_info, headers=nutritionix_header)
print(response.text)

header = {"Authorization": f"Bearer {os.environ.get('SHEETY_API')}"}

for workout in response.json()['exercises']:
    google_url = 'https://api.sheety.co/bed2391b4b626481b6b70abde42aa10d/myWorkouts/workouts'

    google_json = {
        'workout': {
            'date': f"{datetime.now().strftime('%d/%m/%Y')}",
            'time': f"{datetime.now().strftime('%X')}",
            'exercise': f"{workout['name'].title()}",
            'duration': f"{workout['duration_min']}",
            'calories': f"{workout['nf_calories']}"
    }}
    google_response = requests.post(url=google_url, json=google_json, headers=header)
    print(google_response.json())

new_response = requests.get(url='https://api.sheety.co/bed2391b4b626481b6b70abde42aa10d/myWorkouts/workouts', headers=header)
print(new_response.json())