from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
web_page = response.text

soup = BeautifulSoup(markup=web_page, features="html.parser")
# article_tag = soup.find(name="a", class_="storylink")
# print(article_tag)
# article_text = article_tag.get_text()
# print(article_text)
# article_link = article_tag.get("href")
# print(article_link)
# article_upvote = soup.find(name="span", class_="score").get_text()
# print(article_upvote)

articles_tag = soup.find_all(name="a", class_="storylink")
articles = [{"text": article.get_text(), "link": article.get("href")} for article in articles_tag]
articles_upvotes = [int(vote.get_text().split()[0]) for vote in soup.find_all(name="span", class_="score")]

highest_vote = max(articles_upvotes)
highest_vote_index = articles_upvotes.index(highest_vote)

for index, article in enumerate(articles):
    if index == highest_vote_index:
        article["vote"] = highest_vote
        print(article)


