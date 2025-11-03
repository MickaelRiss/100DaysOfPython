import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
website = response.text
soup = BeautifulSoup(markup=website, features="html.parser")
titles_tag = soup.find_all(name="h3", class_="title")
titles = [title.get_text() for title in titles_tag]

with open("movies.txt", "a") as file:
    for title in reversed(titles):
        file.write(f"{title}\n")