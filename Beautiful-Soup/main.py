import re
from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')
movie_page = response.text
soup = BeautifulSoup(movie_page, 'html.parser')

# ---------SPLITS TITLE FROM REVIEW LINK-------------#
# THIS METHOD LEAVES OUT THREE MOVIES THAT ARE MISSING REVIEWS
data = soup.find_all("a", text=re.compile("Read Empire's review of "))
movie_titles = [string.text.split("Read Empire's review of ")[1] for string in data]
movie_titles.reverse()

# ---------GETS TITLE DATA FROM IMG ALT TAGS--------#
# THIS METHOD GATHERS A FEW INCORRECT TITLES FROM THE ALT TAGS
gallery = soup.select_one(selector=".listicle-container")
images = gallery.select(selector=".image-container img")
movies = []
for image in images:
    movies.append(image.get("alt"))
movies.reverse()


with open('movie_list.txt', 'w') as movie_list:
    for index, movie in enumerate(movies):
        movie_list.write(f"{index + 1}) {movie} \n")
