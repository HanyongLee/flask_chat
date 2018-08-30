import os
from flask import Flask, request, jsonify #flask 안에 있는 모듈들
import random
#json으로 바꾸기 위해  라이브러리 추가
import json
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def hello():
    return '챗봇페이지 입니다!!!'
    
    
@app.route('/keyboard')
def keyboard():
    
    #keyboard 딕셔너리 생성
    keyboard = {
              "type" : "buttons",
              "buttons" : ["메뉴", "로또", "고양이", "영화", "기사"]
            }
    
    #딕셔너리를 json으로 바꿔서 리턴 해주기 위한 코드
    json_keyboard = json.dumps(keyboard)
    return json_keyboard
    
@app.route('/message', methods = ['POST']) #url로 요청보내면 not allowed 응답. 허가되지 않음
def message():
    # content라는 key의 value를 msg에 저장
    msg = request.json['content'] #사용자가 요청한 content를 json으로 바꿔 msg에 저장
    img_bool = False
    
    if msg == "메뉴":
        menu = ["20층", "멀캠식당", "꼭대기", "급식"]
        return_msg = random.choice(menu)
    
    elif msg == "로또":
        #1~45 리스트
        numbers = list(range(1,46))
        #6개 샘플링
        pick = random.sample(numbers, 6)
        #정렬 후 스트링으로 변환하여 저장
        return_msg = str(sorted(pick)) #text 필드는 string 타입으로만 보내달라고 document에 나와있음
        
    elif msg == "고양이":
        img_bool=True
        url = "https://api.thecatapi.com/v1/images/search?mime_type=jpg"
        req = requests.get(url).json()
        return_msg = "나만 고양이 없어 :("
        img_url= req[0]['url']
    
    elif msg == "영화":
        img_bool = True
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
        
        return_msg = "%s/평점:%s/예매율:%s" %(pick_movie['title'], pick_movie['star'], pick_movie['reserve'])   #"영화 추천!!" + pick_movie['title']
        img_url = pick_movie['img']
    
    elif msg == "기사":
        img_bool = True
        url = "http://clomag.co.kr/search?query="
        req = requests.get(url).text
        doc = BeautifulSoup(req, 'html.parser')
        
        title_tag = doc.select('h4.title')
        writer_tag = doc.select('span.writer > a')
        day_tag = doc.select('span.date')
        img_tag = doc.select('div.cover > a > img.img-responsive')
        url_tag = doc.select('div.cover > a')
        
        article_dic = {}
        for i in range(0,10):
            article_dic[i] = {
                "title" : title_tag[i].text,
                "writer": writer_tag[i].text,
                "day": day_tag[i].text,
                "img": "https:" + img_tag[i].get('src'),
                "url": url_tag[i].get('href')
            }
            
        pick_article = article_dic[random.randrange(0,10)]
        
        return_msg = "%s\n%s\n%s" %(pick_article['title'], pick_article['writer'], pick_article['day'])
        img_url = pick_article['img']
        page_url = pick_article['url']
        
    else:
        return_msg = "현재 지원하지 않는 기능입니다. :)"
    
    if img_bool == True:
        json_return = { #json으로 바꿔서 응답해주기
            "message":{
                "text" : return_msg,
                "photo": {
                    "url":img_url,
                    "width":720,
                    "height":640
                },
                # # 해당 기사 링크
                "message_button": {
                "label": "기사를 보시겠어요?",
                "url": page_url
                }
            },
            "keyboard": {                   
                #keyboard : 자동 응답 메뉴 호출, 메뉴마다 다른 형태 타고 타고 보여주기 위해서 keyboard 여러개 생성
                  "type" : "buttons",
                  "buttons" : ["메뉴", "로또", "고양이", "영화", "기사"]
                }
        }
    else: 
        json_return = { #json으로 바꿔서 응답해주기
        "message":{
            "text" : return_msg
            },
        "keyboard": {                   
            #keyboard : 자동 응답 메뉴 호출, 메뉴마다 다른 형태 타고 타고 보여주기 위해서 keyboard 여러개 생성
              "type" : "buttons",
              "buttons" : ["메뉴", "로또", "고양이", "영화", "기사"]
            }
        }
    
    return jsonify(json_return) # json.dumps == jsonify 기능은 똑같음. dic -> json으로 바꿔줌. 하나의 목적 다른 수단 활용
    
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
