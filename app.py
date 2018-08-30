import os
from flask import Flask, request, jsonify #flask 안에 있는 모듈들
#json으로 바꾸기 위해  라이브러리 추가
import json

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
    
    json_return = { #json으로 바꿔서 응답해주기
        "message":{
            "text" :msg 
            },
        "keyboard": {                   
            #keyboard : 자동 응답 메뉴 호출, 메뉴마다 다른 형태 타고 타고 보여주기 위해서 keyboard 여러개 생성
              "type" : "buttons",
              "buttons" : ["메뉴", "로또", "고양이", "영화"]
            }
    }
    
    return jsonify(json_return) # json.dumps == jsonify 기능은 똑같음. dic -> json으로 바꿔줌. 하나의 목적 다른 수단 활용
    
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
