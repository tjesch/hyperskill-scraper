import requests

from bs4 import BeautifulSoup
url = input()
#print(url)
r = requests.get(url)
#print(r.content)
soup = BeautifulSoup(r.content, 'html.parser')
#print(soup)
p1 = soup.find('h1')
#print(p1)
print(p1.string)
