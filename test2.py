import requests
from bs4 import BeautifulSoup
import random

url = "http://clomag.co.kr/search?query="
req = requests.get(url).text
doc = BeautifulSoup(req, 'html.parser')

title_tag = doc.select('h4.title')
writer_tag = doc.select('span.writer > a')
day_tag = doc.select('span.date')
img_tag = doc.select('div.cover > a > img.img-responsive')

# print(type(title_tag))
# print(len(writer_tag))
# print(len(img_tag))

article_dic = {}
for i in range(0,10):
    article_dic[i] = {
        "title" : title_tag[i].text,
        "writer": writer_tag[i].text,
        "day": day_tag[i].text
        "img": img_tag[i].get('src')
    }
    
pick_article = article_dic[random.randrange(0,10)]

print(pick_article)
    
    