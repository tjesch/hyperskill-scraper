import string

import requests
from bs4 import BeautifulSoup
import os


url = "https://www.nature.com/nature/articles?sort=PubDate&year=2020"

num_pages = input()
print(num_pages)
article_type = input()

for i in range(int(num_pages)):
    n = i+1
    r = requests.get(url+'&page='+str(n))
    soup = BeautifulSoup(r.content, 'html.parser')
    new_dir = 'Page_'+str(n)
    os.mkdir(new_dir)
    os.chdir(new_dir)

    article_links = soup.findAll('article')
    article_metadata = {}
    for article in article_links:
        if article.find('span', class_="c-meta__type", string=article_type):
            title = article.a.text
            title = title.translate(str.maketrans('', '', string.punctuation))
            title = str.replace(title, ' ', '_')
            article_url = "https://www.nature.com"+ article.a.get('href')
            article_metadata.update({title: article_url})
            mini_soup = BeautifulSoup(requests.get(article_url).content, 'html.parser')
            article_file = open(title + '.txt', mode='w+t', encoding='utf-8')
            article_file.write(mini_soup.find('div', class_="c-article-body").text)
            article_file.close()
    os.chdir(os.path.dirname(os.getcwd()))

print(article_metadata)
