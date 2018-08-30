import os
from flask import Flask, request, jsonify #flask 안에 있는 모듈들
import random
#json으로 바꾸기 위해  라이브러리 추가
import json
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    return '챗봇페이지 입니다!!!'
    
    
@app.route('/keyboard')
def keyboard():
    
    #keyboard 딕셔너리 생성
    keyboard = {
              "type" : "buttons",
              "buttons" : ["메뉴", "로또", "고양이", "영화"]
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
        cat_url= req[0]['url']
        
    else:
        return_msg = "현재 메뉴만 지원합니다 :)"
    
    if img_bool == True:
        json_return = { #json으로 바꿔서 응답해주기
            "message":{
                "text" : "나만 고양이 없어 :(",
                "photo": {
                    "url":cat_url,
                    "width":720,
                    "height":640
                }
                },
            "keyboard": {                   
                #keyboard : 자동 응답 메뉴 호출, 메뉴마다 다른 형태 타고 타고 보여주기 위해서 keyboard 여러개 생성
                  "type" : "buttons",
                  "buttons" : ["메뉴", "로또", "고양이", "영화"]
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
              "buttons" : ["메뉴", "로또", "고양이", "영화"]
            }
        }
    
    return jsonify(json_return) # json.dumps == jsonify 기능은 똑같음. dic -> json으로 바꿔줌. 하나의 목적 다른 수단 활용
    
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
