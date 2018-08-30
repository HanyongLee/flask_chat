# 내가 연습한 것
import requests
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/running/current.nhn"
req = requests.get(url).text
doc = BeautifulSoup(req, 'html.parser')

title_tag = doc.select('dt.tit > a')


return_stars = doc.select('dd.star > dl.info_star > dd > div.star_t1 > a > span.num')
return_resurve = doc.select(' div.star_t1 > span.num ')

list_movies = []
list_stars= []
list_resurve = []

for i in return_doc:
     list_movies.append(i.text)
print(list_movies)

for i in return_stars:
     list_stars.append(i.text)
print(list_stars)

for i in return_resurve:
     list_resurve.append(i.text)
print(list_resurve)

    
# return_msg = doc.select('#content > div.article > div > div.lst_wrap > ul > li > dl > dt > a').text
# print(return_msg)

# return_msg = doc.select('#content > div.article > div > div.lst_wrap > ul > li > dl > dd.star > dl.info_star > dd > div > a > span.num')[0]
# print(return_msg)

# return_msg = doc.select(#content > div.article > div > div.lst_wrap > ul > li > div > a > img)
# print(return_msg)