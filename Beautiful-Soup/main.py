import re
from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')
movie_page = response.text

soup = BeautifulSoup(movie_page, 'html.parser')


gallery = soup.select_one(selector=".listicle-container")
all_images = gallery.select(selector=".image-container img")
all_movies = []
for image in all_images:
    all_movies.append(image.get("alt"))
all_movies.reverse()


with open('movie_list.txt', 'w') as movie_list:
    for index, movie in enumerate(all_movies):
        movie_list.write(f"{index + 1}) {movie} \n")
