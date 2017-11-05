# -*- coding: utf-8 -*-
# python 2.7

import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def Welcome():
    return app.send_static_file('index.html')

@app.route('/keyboard')
def Keyboard():
    # 유저가 최초로 채팅방에 들어온 경우.
    message = {
            'type': 'text'
    }
    return jsonify(message)

@app.route('/message', methods=['POST'])
def GetMessage():
    # 유저가 보낸 메시지 정보 (dict)
    received_data = request.get_json()

    # 유저 메시지 중 텍스트 부분 (string)
    echo_text = received_data['content']

    message = {
        "message": {
            "text": echo_text,
        }
    }
    return jsonify(message), 200, {'ContentType':'application/json'} 

@app.route('/friend', methods=['POST'])
def FriendAdd():
    # 친구 추가 했을 시
    # 내맘대로 코딩하는 부분
    # 예를 들어 슬랙으로 친구 추가 알림을 보낸다던지...
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

@app.route('/friend', methods=['DELETE'])
def FriendDelete():
    # 친구 삭제 했을 시
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

@app.errorhandler(404)
def page_not_found(e):
    error_message = {
        "message": {
            "text": '잘못된 접근입니다!'
        }
     }
    return jsonify(error_message)

if __name__ == "__main__":
    # 미리 설정된 포트가 없으면 5000번 이용
    # port = os.getenv('PORT', '5000')

    # 플라스크 서버 실행
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
