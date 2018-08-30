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
url_tag = doc.select('div.cover > a')

# print(type(title_tag))
# print(len(writer_tag))
# print(len(url_tag))

article_dic = {}
for i in range(0,10):
    article_dic[i] = {
        "title" : title_tag[i].text,
        "writer": writer_tag[i].text,
        "day": day_tag[i].text,
        "img": "https:" + img_tag[i].get('src'),    # src 데이터만 가져오기
        "url": url_tag[i].get('href')               # href 데이터만 가져오기
    }
    
pick_article = article_dic[random.randrange(0,10)]

print(pick_article)
    
    