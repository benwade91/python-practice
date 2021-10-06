import os
import requests

nutritionix_ep = 'https://trackapi.nutritionix.com/v2/natural/exercise'

nutritionix_header = {
    'x-app-id': os.environ.get('NUTRITION-X-APP-ID'),
    'x-app-key': os.environ.get('NUTRITION-API-KEY')
}
user_info = {
 "query":"ran 3 miles",
 "gender":"female",
 "weight_kg":72.5,
 "height_cm":167.64,
 "age":30
}

response = requests.post(url=nutritionix_ep, json=user_info, headers=nutritionix_header)
print(response.text)