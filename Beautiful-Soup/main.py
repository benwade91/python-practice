from bs4 import BeautifulSoup

with open('website.html') as html:
    contents = html.read()

soup = BeautifulSoup(contents, 'html.parser')

print(soup.title.name)