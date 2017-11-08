## ChatFlow API v. 1.0 개요
이 문서는 ChatFlow를 통하여 챗봇을 개발하고자 할 때 사용되는 API에 대해 기술합니다.

## 1. 이용에 대한 참고사항

  1. **client_id**와 **app_id**는 외부에 노출되지 않도록 주의해 주시기 바랍니다.
  2. ChatFlow API를 이용해 옐로아이디/톡톡친구 챗봇을 구현한 프레임워크 별 예제 코드
     - Flask
     - Ruby on Rails

## 2. 개인정보 수집 및 이용에 대한 안내사항

  1. 회원이 ChatFlow API 플랫폼 서비스를 이용하는 과정에서 이용자의 개인정보 수집이 필요한 경우, 이용자로부터 개인정보 수집 및 이용에 대한 명시적인 동의를 받아야 합니다.
  2. ChatFlow는 '[개인정보 취급위탁 동의](https://center-pf.kakao.com/entrustment)'에 따라 안전하게 개인정보 처리 업무를 진행합니다.

## 3. 이용 시작하기
#### 3.1. ChatFlow 가입
ChatFlow에서 API를 사용하기 위해서는 먼저 Client ID 발급을 위한 회원가입을 진행해야 합니다.

1. 웹사이트에서의
2. 회원가입 절차를
3. 여러 단계에 걸쳐
4. 서술한다
5. 앱 정보와 모니터링 메시지를 수신할 전화번호를 입력하고, 개인정보 수집 및 이용에 동의한 뒤 정보를 저장하여 앱을 생성합니다.

#### 3.2. ChatFlow 상태관리 API 서비스 시작
회원가입이 완료되어 서비스 가능한 상태가 되면, 다음 단계에 따라 서비스를 시작할 수 있습니다.

  1. 챗봇 시나리오 API 사용 방법을
  2. 여러 단계에 나누어
  3. 서술한다

#### 3.3. API 클라이언트 테스트
챗봇 시나리오를 생성하면 개발 서버에서 직접 ChatFlow API를 실행할 수 있습니다.

카카오 옐로아이디 / 네이버 톡톡친구 뿐만 아니라 각종 웹/어플리케이션 개발 시에도 범용적으로 사용 가능합니다.

관리자 페이지에서도 테스트를 실행할 수 있습니다.

 - 특정 챗봇 시나리오의 유저가 5분 이내로 메시지를 보내지 않는 경우 해당 유저의 챗봇 시나리오는 entry node부터 다시 시작합니다.
 - ​

## 4. 용어 설명

#### 4.1. ChatFlow API
- ChatFlow 이용자가 특정 시나리오 상의 유저 상태를 제어하는 API입니다.
- http(s) restful api를 통하여 개발 서버 -> ChatFlow 서버를 호출합니다.

#### 4.2. client_id
- ChatFlow에서 회원가입 시 클라이언트에게 발급되는 고유 ID 값입니다.
- 클라이언트를 식별하기 위해 ChatFlow API 호출 시 매번 포함해야 하는 값입니다.


#### 4.3. app_id
- 클라이언트의 챗봇 시나리오를 식별할 수 있는 고유 ID 값입니다.
- client_id와 함께 ChatFlow API 호출 시 함께 포함해야 하는 값입니다.

#### 4.4. user\_key
- 클라이언트의 특정 챗봇 시나리오 내의 사용자를 식별하기 위한 값입니다.
- 서비스 개발 서버에서는 API 호출 시 각 사용자의 고유 키를 함께 전달해주어야 합니다.
- user\_key는 각각의 서비스 이용자에 대해 발급된 고유한 값이어야 합니다.




## 5. API specifications

- 카카오 플러스친구 API 서버에서 개발사 서버를 호출하는 API에 대한 명세서입니다.
- 개발사는 아래 스펙에 맞춰서 http(s) 서버를 구축하셔야 합니다.
- 응답 지연시간 : 최대 5초안에 응답이 오지 않는 경우 응답없음 메시지가 사용자에게 발송됩니다.
- QoS : 만약 응답 실패가 10회 이상 발생하게 되면 자동적으로 해당 모듈은 지정된 장애 메시지를 리턴하게 됩니다. 더불어 앱 등록시 지정된 관리자에게 카카오톡으로 장애 메시지가 발송됩니다.
- [플러스친구 운영도구](https://center-pf.kakao.com)를 통해 설정한 개발사 서버 URL을 호출하게 됩니다.
- 개발사 서버가 방화벽으로 보호되고 있는경우 [Server information](https://github.com/plusfriend/auto_reply#7-server-information) 문서를 참고해주세요.


#### 5.1. Home Keyboard API
- 이용자가 최초로 채팅방에 들어올 때 기본으로 키보드 영역에 표시될 자동응답 명령어의 목록을 호출하는 API입니다.
- 챗팅방을 지우고 다시 재 진입시에도 호출됩니다. 다만 카카오 서버에서도 1분동안 캐쉬가 저장되기 때문에 유저가 채팅방을 지우고 들어오는 행동을 반복하더라도 개발사 서버를 1분에 한번씩 호출하게 됩니다. 즉, 개발사 서버에서 정보가 변경되어도 최대 1분뒤에 유저들에게 반영이 됩니다.
- 유저가 자동응답으로 메시지를 주고 받았을 경우는 마지막 메시지에 담겨있던 자동응답 명령어 목록이 표시됩니다. 다만 메시지에 저장된 자동응답 명령어는 10분간 유효합니다. 10분이 지난 다음에는 다시 keyboard api를 호출하여 자동응답 목록을 초기화하게 됩니다.


##### Specification
- **Method** : GET
- **URL** : http(s)://:your\_server\_url/keyboard
- **Content-Type** : application/json; charset=utf-8
- **예제**
```
curl -XGET 'https://:your_server_url/keyboard'
```
- **Response**

| 필드명      | 타입                                       | 필수여부     | 설명                                       |
| -------- | ---------------------------------------- | -------- | ---------------------------------------- |
| keyboard | [Keyboard](https://github.com/plusfriend/auto_reply#6-object) | Required | 키보드 영역에 표현될 버튼에 대한 정보. 생략시 ```text``` 타입이 선택된다. |
- **예제**
```
{
    "type" : "buttons",
    "buttons" : ["선택 1", "선택 2", "선택 3"]
}
```

#### 5.2. 메시지 수신 및 자동응답 API
- 사용자가 선택한 명령어를 파트너사 서버로 전달하는 API입니다.
- 자동응답 명령어에 대한 답변은 응답 메시지(Message)와 응답 메시지에 따른 키보드 영역의 답변 방식(Keyboard)의 조합으로 이루어집니다. 답변 방식은 주관식(text)과 객관식(buttons) 중 선택할 수 있습니다.
- 자동응답을 통해 친구에게 미디어 타입(사진/동영상/오디오)을 받고자 하는 경우 주관식 키보드(text)를 선택하세요. 메시지를 통해 <‘+’버튼을 눌러 미디어를 전송하세요>와 같이 안내하는 것이 필요 할 수 있습니다.
- 유저가 보낸 미디어 타입의 카카오 서버에서의 보존기간은 아래와 같습니다.
  - 음성파일 : 20일
  - 이미지파일 : 20일
  - 비디오 : 20일
- 미디어 파일의 보존기간은 서버의 상황에 의하여 변동 될 수 있습니다.

##### Specification
- **Method** : POST
- **URL** : http(s)://:your\_server\_url/message
- **Content-Type** : application/json; charset=utf-8
- **Parameters**

| 필드명       | 타입     | 필수여부     | 설명                              |
| --------- | ------ | -------- | ------------------------------- |
| user\_key | String | Required | 메시지를 발송한 유저 식별 키                |
| type      | String | Required | text, photo                     |
| content   | String | Required | 자동응답 명령어의 메시지 텍스트 혹은 미디어 파일 uri |
- **예제**
```
curl -XPOST 'https://:your_server_url/message' -d '{
  "user_key": "encryptedUserKey",
  "type": "text",
  "content": "차량번호등록"
}'
```
```
curl -XPOST 'https://your_server_url/message' -d '{
  "user_key": "encryptedUserKey",
  "type": "photo",
  "content": "http://photo_url/number.jpg"
}'
```
- **Response**

| 필드명      | 타입                                       | 필수여부     | 설명                                       |
| -------- | ---------------------------------------- | -------- | ---------------------------------------- |
| message  | [Message](https://github.com/plusfriend/auto_reply/blob/master/README.md#62-message) | Required | 자동응답 명령어에 대한 응답 메시지의 내용. 6.2에서 상세 기술     |
| keyboard | [Keyboard](https://github.com/plusfriend/auto_reply#6-object) | Optional | 키보드 영역에 표현될 명령어 버튼에 대한 정보. 생략시 text 타입(주관식 답변 키보드)이 선택된다. 6.1에서 상세 기술 |
- **예제**
```
{
    "message":{
        "text" : "귀하의 차량이 성공적으로 등록되었습니다. 축하합니다!"
    }
}
```
```
{
  "message": {
    "text": "귀하의 차량이 성공적으로 등록되었습니다. 축하합니다!",
    "photo": {
      "url": "https://photo.src",
      "width": 640,
      "height": 480
    },
    "message_button": {
      "label": "주유 쿠폰받기",
      "url": "https://coupon/url"
    }
  },
  "keyboard": {
    "type": "buttons",
    "buttons": [
      "처음으로",
      "다시 등록하기",
      "취소하기"
    ]
  }
}
```

#### 5.3. 친구 추가/차단 알림 API
- 특정 카카오톡 이용자가 플러스친구를 친구로 추가하거나 차단하는 경우 해당 정보를 파트너사 서버로 전달하는 API입니다.

##### Specification
- **Method** : POST / DELETE
- **URL** : http(s)://:your\_server\_url/friend
- **Content-Type** : application/json; charset=utf-8
- **Parameters**

| 필드명       | 타입     | 필수여부     | 설명     |
| --------- | ------ | -------- | ------ |
| user\_key | String | Required | 유저 식별키 |
- **Response**

| http status code | code | message | comment |
| ---------------- | ---- | ------- | ------- |
| 200              | 0    | SUCCESS | 정상 응답   |
- **예제**
 - *친구 추가*
```
curl -XPOST 'https://:your_server_url/friend' -d '{"user_key" : "HASHED_USER_KEY" }'
```
 - *친구 삭제*
```
curl -XDELETE 'https://:your_server_url/friend/:user_key'
```

#### 5.4. 채팅방 나가기
- 사용자가 채팅방 나가기를 해서 채팅방을 목록에서 삭제했을 경우 해당 정보를 파트너사 서버로 전달하는 API입니다.

##### Specification
- **Method** : DELETE
- **URL** : http(s)://:your\_server\_url/chat\_room/:user\_key
- **Content-Type** : application/json; charset=utf-8
- **Response**

| http status code | code | message | comment |
| ---------------- | ---- | ------- | ------- |
| 200              | 0    | SUCCESS | 정상 응답   |
- **예제**
```
curl -XDELETE 'https://:your_server_url/chat_room/HASHED_USER_KEY'
```

## 6. Object

##### 6.1. Keyboard

 - 응답 메시지에 따라 사용자의 키보드 영역에 표현될 메시지 입력방식에 대한 정보입니다.
 - 별도로 설정하지 않는 경우 text 타입이 기본으로 설정됩니다.

| 필드명     | 타입            | 필수여부     | 설명                                       |
| ------- | ------------- | -------- | ---------------------------------------- |
| type    | String        | Required | buttons: 객관식 응답의 목록을 구성할 수 있음 <br/>text: 주관식 응답을 입력받을 수 있음 |
| buttons | Array[String] | Optional | 객관식 응답 내용의 목록                            |

 - 직접 입력
```
{
  "type": "text"
}
```
 - 버튼 입력

```
{
  "type": "buttons",
  "buttons": [
    "선택 1",
    "선택 2",
    "선택 3"
  ]
}
```


##### 6.2. Message

 - 카카오톡 이용자가 명령어를 선택 혹은 입력했을 때 이용자에게 전송하는 응답 메시지입니다.
 - String, photo, MessageButton의 조합으로 이루어집니다.
 - 3가지 타입 중 1개 이상이 반드시 들어가야 하며, 최대 3가지 타입 모두 포함될 수 있습니다.

| 필드명            | 타입                                       | 필수여부     | 설명                                       |
| -------------- | ---------------------------------------- | -------- | ---------------------------------------- |
| text           | String                                   | Optional | 사용자에게 발송될 메시지 텍스트(최대 1000자)              |
| photo          | [Photo](https://github.com/plusfriend/auto_reply/blob/master/README.md#63-photo) | Optional | 말풍선에 들어갈 이미지 정보. 1장 제한, JPEG/PNG 포맷. 6.3에서 상세 기술 |
| message_button | [MessageButton](https://github.com/plusfriend/auto_reply/blob/master/README.md#621-messagebutton) | Optional | 말풍선에 붙는 링크버튼 정보. 6.2.1에서 상세 기술           |

```
{
  "text": "안녕하세요.",
  "photo": {
    "url": "https://hello.photo.src",
    "width": 640,
    "height": 480
  },
  "message_button": {
    "label": "반갑습니다.",
    "url": "http://hello.world.com/example"
  }
}
```
###### 6.2.1. MessageButton

 - 응답 메시지의 말풍선 하단에 보여지는 링크버튼 정보입니다.

| 필드명   | 타입     | 필수여부     | 설명             |
| ----- | ------ | -------- | -------------- |
| label | String | Required | 링크버튼의 타이틀      |
| url   | String | Required | 링크버튼의 연결 링크 주소 |

```
{
  "label": "쿠폰확인하기",
  "url": "http://coupon.coupon.com/~~"
}
```

##### 6.3. Photo

 - 이미지 정보

| 필드명    | 타입     | 필수여부     | 설명         |
| ------ | ------ | -------- | ---------- |
| url    | String | Required | 이미지 url    |
| width  | Int    | Required | 이미지 width  |
| height | Int    | Required | 이미지 height |

> 이미지 권장 사이즈 : 720 x 630px  
> 지원 파일형식 및 권장 용량 : jpg, png /500KB

```
{
  "url": "https://photo.src",
  "width": 640,
  "height": 480
}
```

## 7. Server information

| host                   | port | comment          |
| ---------------------- | ---- | ---------------- |
| https://ybot.kakao.com | 443  | https api server |

### 7.1. Proxy Server information
카카오에서 파트너사 서버를 호출하는 경우 아래 3대의 proxy서버를 통하게 됩니다. 파트너사 방화벽 설정을 하게 될 경우 아래 3개의 IP에 대한 ACL을 허용해주시기 바랍니다.

| IP             |
| -------------- |
| 110.76.143.234 |
| 110.76.143.235 |
| 110.76.143.236 |

## 8. Response Code
##### Success Response

| http status code | code | message | comment |
| ---------------- | ---- | ------- | ------- |
| 200              | 0    | SUCCESS | 정상 응답   |

##### Error Response

| http status code | code | comment                       |
| ---------------- | ---- | ----------------------------- |
| 400              | 100  | bad request                   |
| 400              | 201  | wrong api key                 |
| 400              | 202  | wrong bot url                 |
| 503              | 203  | wrong message format          |
| 408              | 204  | request timeout               |
| 408              | 204  | wrong keyboard initialization |
| 400              | 301  | profile not found             |
| 400              | 302  | user not found                |
| 400              | 303  | not user friend               |
| 400              | 400  | unsupported media type        |



## 9. 질의응답
상단의 issue를 통해서 문의주시길 바랍니다.
- https://github.com/plusfriend/auto_reply/issues