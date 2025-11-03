from bs4 import BeautifulSoup

with open("website.html") as f:
    contents = f.read()

soup = BeautifulSoup(markup=contents, features="html.parser")
all_anchor_a = soup.find_all(name="a")

# for tag in all_anchor_a:
#     print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)