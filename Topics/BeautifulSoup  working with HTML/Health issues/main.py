import re
import requests

from bs4 import BeautifulSoup

url = input()
r = requests.get(url)
letter = 'S'
soup = BeautifulSoup(r.content, 'html.parser')
ListOfTitles = soup.findAll("a", attrs={'href': re.compile("topic|entity")})
ListToReturn = []
for obj in ListOfTitles:
    if obj.contents:
        a = obj.contents[0].string
        if a is not None and a[0] == letter and len(a) > 1:
            ListToReturn.append(a)
print(ListToReturn)
