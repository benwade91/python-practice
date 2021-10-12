import requests
from bs4 import BeautifulSoup


# search_date = input("Input a date to search YYYY-MM-DD")
search_date = "1991-10-25"
response = requests.get(f"https://www.billboard.com/charts/hot-100/{search_date}")

soup = BeautifulSoup(response.text, 'html.parser')

song_title = [song.text for song in soup.find_all(class_="chart-element__information__song")]
artist = [artist.text for artist in soup.find_all(class_="chart-element__information__artist")]
print(artist)