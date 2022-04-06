import requests

from bs4 import BeautifulSoup

index = int(input())
url = input()

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
subtitles = soup.findAll('h2')
IndexSubtitle = subtitles[index].text
print(IndexSubtitle)
