# 파이썬 챗봇 만들기

### 카카오톡 플러스친구 관리자센터

- 플러스 친구 생성 후 공개설정(공개 안되면 검색안됨 !!!)
- 스마트 챗팅 API형 사용

### C9 개발

- 우측 상단의 톱니바퀴에 들어가서 python3로 설정변경
- `sudo pip3 install flask` 플라스크 설치

### keyboard
```python3
import os
from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return '챗봇페이지 입니다!!!'
    
    
@app.route('/keyboard')
def keyboard():
    keyboard = {
              "type" : "buttons",
              "buttons" : ["메뉴", "로또", "고양이", "영화"]
            }
    json_keyboard = json.dumps(keyboard)
    return json_keyboard
    
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))

```

### API

- request
    - url: 어떤 경로로 보낼꺼니?
    - method: 어떤 방법으로 보낼꺼니?
    - parameter: 어떤 정보를 담을꺼니?

- response
    - data type: 어떤 형식으로 답할까?
    - 

### 신간 기사 추천 서비스
- 구현하고 싶은 것
    -10개 뽑은 것 중 중복되지 않게 기사 보여주기
    -서버 요청시 마다 새롭게 random 돌리는데 기존에 봤던 것을 확인하려면 DB가 필요하겠다.