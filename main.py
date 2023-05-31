import bs4
import requests

HUBS = ['Python *', 'Java *']

HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
      }

url = 'https://habr.com'

response = requests.get(url, headers=HEADERS)
text = response.text

soup = bs4.BeautifulSoup(text, features="html.parser")

articles = soup.find_all("article")
for article in articles:
    hubs = article.find_all(class_="tm-article-snippet__hubs-item-link")
    hubs = [hub.text.strip() for hub in hubs]
    for hub in hubs:
        if hub in HUBS:
            href = article.find(class_="tm-title__link").attrs["href"]
            title = article.find("h2").find("span").text
            result = f'{title} ==> {url}{href}'
            print(result)