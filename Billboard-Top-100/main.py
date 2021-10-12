import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from bs4 import BeautifulSoup
from pprint import pprint

search_date = input("Input a date to search YYYY-MM-DD")
# search_date = "1991-10-25"
search_year = search_date.split('-')[0]
response = requests.get(f"https://www.billboard.com/charts/hot-100/{search_date}")

soup = BeautifulSoup(response.text, 'html.parser')

song_title = [song.text for song in soup.find_all(class_="chart-element__information__song")]
artist = [artist.text for artist in soup.find_all(class_="chart-element__information__artist")]
song_queries = [f"spotify:track:{song} year:{search_year}" for song in song_title]


auth = SpotifyOAuth(client_secret=os.environ.get('SPOTIPY_CLIENT_SECRET'),
                    client_id=os.environ.get('SPOTIPY_CLIENT_ID'),
                    redirect_uri=os.environ.get('SPOTIPY_REDIRECT_URI'),
                    scope="playlist-modify-private,playlist-modify-public", )

spotify = spotipy.Spotify(oauth_manager=auth)

song_ids = []
for song in song_title:
    try:
        song_ids.append(f"spotify:track:{spotify.search(q=f'track:{song} year:{search_year}', type='track')['tracks']['items'][0]['id']}")
    except:
        print(f"{song} didnt work")

client = spotipy.client.Spotify(oauth_manager=auth)
user_id = client.current_user()['id']
new_playlist = client.user_playlist_create(user='benn925', name=f'{search_date} Spotipy')
try:
    print(client.playlist_add_items(playlist_id=new_playlist['id'], items=song_ids, position=0))
except:
    print("exceptions")


