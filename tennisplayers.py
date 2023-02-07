import requests
from bs4 import BeautifulSoup as bs

headers = {
    'User-Agent': 'Mozilla/5.0',
}

file = requests.get("https://howtheyplay.com/individual-sports/Top-10-Greatest-Male-Tennis-Players-of-All-Time",headers=headers)

soup = bs(file.content, 'html.parser')
print(soup.prettify)
# players = soup.find_all("h2")
# print(players)