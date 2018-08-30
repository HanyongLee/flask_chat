# 강사님 코드 

import requests
from bs4 import BeautifulSoup
import random

url = "https://movie.naver.com/movie/running/current.nhn"
req = requests.get(url).text
doc = BeautifulSoup(req, 'html.parser')

title_tag = doc.select('dt.tit > a')
star_tag = doc.select('div.star_t1 > a > span.num') # bs4 문법은 중간에 a 하나 생략되도 인식 못함, 부등호도 띄어서 써줘야함
reserve_tag = doc.select('div.star_t1.b_star > span.num')  # class가 두개이면 공백에 .으로 연결시키면됨
img_tag = doc.select('div.thumb > a > img')

movie_dic = {}
for i in range(0,10):
    movie_dic[i] = {
        "title": title_tag[i].text,
        "star": star_tag[i].text,
        "reserve": reserve_tag[i].text,
        "img": img_tag[i].get('src') #bs4의 method -> 구글링 검색어 "bs4 get src or bs4 get attribute value"
    }

pick_movie = movie_dic[random.randrange(0,10)]

print(pick_movie) #dictionary가 순서가 없음
