## ChatFlow API v. 1.0 개요
이 문서는 ChatFlow를 통하여 챗봇을 개발하고자 할 때 사용되는 API에 대해 기술합니다.

## 1. 이용에 대한 참고사항

1. **developer_id**와 **app_id**는 외부에 노출되지 않도록 주의해 주시기 바랍니다.

2. ChatFlow API를 이용해 옐로아이디/톡톡친구 챗봇을 구현한 프레임워크 별 예제 코드

   - [Flask](https://github.com/lesimor/ChatFlow/tree/master/example/flask)
   - [Ruby on Rails](https://github.com/lesimor/ChatFlow/tree/master/example/ROR)

   <br/>
## 2. 개인정보 수집 및 이용에 대한 안내사항

1. 회원이 ChatFlow API 플랫폼 서비스를 이용하는 과정에서 이용자의 개인정보 수집이 필요한 경우, 이용자로부터 개인정보 수집 및 이용에 대한 명시적인 동의를 받아야 합니다.
2. ChatFlow는 '[개인정보 취급위탁 동의](https://center-pf.kakao.com/entrustment)'에 따라 안전하게 개인정보 처리 업무를 진행합니다.

<br/>

## 3. 이용 시작하기
#### 3.1. ChatFlow 가입
ChatFlow에서 API를 사용하기 위해서는 먼저 Client ID 발급을 위한 회원가입을 진행해야 합니다.

1. 웹사이트의 회원가입 페이지에서 **회원가입을 진행**합니다.
   - http://chatflow.ai/clients/sign_up
2. **나의 ChatFlow 목록** 페이지가 뜨면 회원가입 절차가 완료된 것입니다.
3. 내 정보 페이지에서 자신에게 부여된 developer_id를 확인할 수 있습니다.

#### 3.2. ChatFlow 상태관리 API 서비스 시작
회원가입이 완료되어 서비스 가능한 상태가 되면, 다음 단계에 따라 서비스를 시작할 수 있습니다.

1. 나의 ChatFlow 목록 페이지에서 **ChatFlow 추가 버튼**을 클릭합니다.
2. **이름**과 **설명**을 입력합니다.
3. **ChatFlow 관리 페이지**에서 발급된 **conversation_id**를 확인합니다.

</br>

#### 3.3. API 클라이언트 테스트
챗봇 시나리오를 생성하면 개발 서버에서 직접 ChatFlow API를 실행할 수 있습니다.

카카오 옐로아이디 / 네이버 톡톡친구 뿐만 아니라 각종 웹/어플리케이션 개발 시에도 범용적으로 사용 가능합니다.

ChatFlow 관리 페이지에서도 테스트를 실행할 수 있습니다.

</br>

## 4. 용어 설명

#### 4.1. ChatFlow API
- ChatFlow 이용자가 특정 시나리오 상의 유저 상태를 제어하는 API입니다.
- http(s) restful api를 통하여 **개발 서버 -> ChatFlow 서버**를 호출합니다.

#### 4.2. developer_id

- ChatFlow에서 회원가입 시 **개발자 계정에 발급되는 고유 ID** 값입니다.
- 개발자를 식별하기 위해 ChatFlow **API 호출 시 매번 포함해야 하는 값**입니다.


#### 4.3. app_id
- 개발자의 챗봇 **시나리오를 식별할 수 있는 고유 ID** 값입니다.
- developer_id와 함께 ChatFlow **API 호출 시 함께 포함해야 하는 값**입니다.

#### 4.4. user\_id
- 개발자 챗봇 **시나리오 내의 사용자를 식별하기 위한 값**입니다.
- 개발사 서버에서는 **API 호출 시 각 사용자의 고유 키를 함께 전달**해주어야 합니다.
- user\_id는 **각각의 서비스 이용자에 대해 발급된 고유한 값**이어야 합니다.


</br>

## 5. API specifications

- 개발사 서버에서 ChatFlow 서버를 호출하는 API에 대한 명세서입니다.


### 5.1. 유저 메세지 입력 API
- 개발사의 애플리케이션 사용자가 입력한 메시지를 ChatFlow 서버로 전달하는 API입니다.

<br/>

#### 요청

- **Method** : POST
- **URL** : http://chatflow.ai/api/v1/message
- **Content-Type** : application/json; charset=utf-8
- **Parameters**

| 필드명          | 타입     | 필수여부     | 설명                             |
| ------------ | ------ | -------- | ------------------------------ |
| developer_id | String | Required | **개발자 식별 ID**                  |
| app_id       | String | Required | 개발자의 챗봇 **시나리오 식별 ID**         |
| user_id      | String | Required | 개발자 애플리케이션 내의 **사용자 식별 ID**    |
| message      | String | Required | 개발자 애플리케이션 내의 **사용자가 입력한 메시지** |
<br/>

#### 응답

|   필드명    |                    타입                    |   필수여부   | 설명                                       |
| :------: | :--------------------------------------: | :------: | :--------------------------------------- |
|    id    |                  String                  | Required | 챗봇 시나리오 상의 노드 ID, 관리자 페이지에서 확인 가능.       |
|  action  |                  String                  | Required | 노드의 액션 타입, < intent\|select\|slot\|link\|custom > |
| message  | [Message](https://github.com/plusfriend/auto_reply/blob/master/README.md#62-message) | Required | 자동응답 명령어에 대한 응답 메시지의 내용. 6.1에서 상세 기술     |
| keyboard | [Keyboard](https://github.com/plusfriend/auto_reply#6-object) | Required | 키보드 영역에 표현될 명령어 버튼에 대한 정보. 생략시 text 타입(주관식 답변 키보드)이 선택된다. 6.2에서 상세 기술 |
|   slot   |                   Slot                   | Required | 대화를 진행하면서 축적된 정보, slot 노드를 거치면서 축적된다.    |
- **예제**
```
{
	"id": "qsYGKEUPKO",
	"action": "slot",
	"message": {
		"text": "주소를 알려주세요.",
		"image": null
	},
	"keyboard": {
		"type": "text"
	},
	"slot": {
		"커피": "아메리카노",
		"사이즈": "톨"
	}
}
```
```
{
	"id": "DeBOArSUaB",
	"action": "select",
	"message": {
		"text": "귀하의 성별을 알려주세요",
		"image": null
	},
	"keyboard": {
		"type": "buttons",
		"buttons": [
          "여자",
          "남자
		]
	},
	"slot": {}
}
```

</br>

### 5.2. 유저 상태 초기화

- 서비스되는 애플리케이션에서 예외 상황이 발생한 경우 유저의 상태를 시나리오 상의 entry로 전이하는 API입니다.

#### 요청
- **Method** : POST
- **URL** : http://chatflow.ai/api/v1/init
- **Content-Type** : application/json; charset=utf-8
- **Parameters**

| 필드명          | 타입     | 필수여부     | 설명                          |
| ------------ | ------ | -------- | --------------------------- |
| developer_id | String | Required | **개발자 식별 ID**               |
| app_id       | String | Required | 개발자의 챗봇 **시나리오 식별 ID**      |
| user_id      | String | Required | 개발자 애플리케이션 내의 **사용자 식별 ID** |

<br/>

#### 응답

|   필드명    |                    타입                    |   필수여부   | 설명                                       |
| :------: | :--------------------------------------: | :------: | :--------------------------------------- |
|    id    |                  String                  | Required | 챗봇 시나리오 상의 노드 ID, 관리자 페이지에서 확인 가능.       |
|  action  |                  String                  | Required | 노드의 액션 타입, < intent\|select\|slot\|link\|custom > |
| message  | [Message](https://github.com/plusfriend/auto_reply/blob/master/README.md#62-message) | Required | 자동응답 명령어에 대한 응답 메시지의 내용. 6.2에서 상세 기술     |
| keyboard | [Keyboard](https://github.com/plusfriend/auto_reply#6-object) | Required | 키보드 영역에 표현될 명령어 버튼에 대한 정보. 생략시 text 타입(주관식 답변 키보드)이 선택된다. 6.1에서 상세 기술 |
|   slot   |                   Slot                   | Required | 대화를 진행하면서 축적된 정보, slot 노드를 거치면서 축적된다.    |

- **예제**

```
{
	"id": "qsYGKEUPKO",
	"action": "intent",
	"message": {
		"text": "안녕하세요. 무엇을 도와드릴까요?",
		"image": null
	},
	"keyboard": {
		"type": "text"
	},
	"slot": {}
}
```

</br>

### 5.3. 특정 노드로 상태 전이

- 시나리오 상의 특정 노드로 사용자의 상태를 강제로 변경해야 하는 경우 호출하는 API 입니다.

#### 요청

- **Method** : POST
- **URL** : http://chatflow.ai/api/v1/init
- **Content-Type** : application/json; charset=utf-8
- **Parameters**

| 필드명          | 타입     | 필수여부     | 설명                          |
| ------------ | ------ | -------- | --------------------------- |
| developer_id | String | Required | **개발자 식별 ID**               |
| app_id       | String | Required | 개발자의 챗봇 **시나리오 식별 ID**      |
| user_id      | String | Required | 개발자 애플리케이션 내의 **사용자 식별 ID** |
| node_id      | String | Required | 이동하고자 하는 **노드 ID**          |

<br/>

#### 응답

|   필드명    |                    타입                    |   필수여부   | 설명                                       |
| :------: | :--------------------------------------: | :------: | :--------------------------------------- |
|    id    |                  String                  | Required | 챗봇 시나리오 상의 노드 ID, 관리자 페이지에서 확인 가능.       |
|  action  |                  String                  | Required | 노드의 액션 타입, < intent\|select\|slot\|link\|custom > |
| message  | [Message](https://github.com/plusfriend/auto_reply/blob/master/README.md#62-message) | Required | 자동응답 명령어에 대한 응답 메시지의 내용. 6.1에서 상세 기술     |
| keyboard | [Keyboard](https://github.com/plusfriend/auto_reply#6-object) | Required | 키보드 영역에 표현될 명령어 버튼에 대한 정보. 생략시 text 타입(주관식 답변 키보드)이 선택된다. 6.2에서 상세 기술 |
|   slot   |                   Slot                   | Required | 대화를 진행하면서 축적된 정보, slot 노드를 거치면서 축적된다.    |

- **예제**

```
{
	"id": "qsYGKEUPKO",
	"action": "intent",
	"message": {
		"text": "안녕하세요. 무엇을 도와드릴까요?",
		"image": null
	},
	"keyboard": {
		"type": "text"
	},
	"slot": {}
}
```

</br>

## 6. Object

##### 6.1. Message

- ChatFlow 연동 서비스 이용자가 명령어를 선택 혹은 입력했을 때 이용자에게 전송하는 응답 메시지입니다.
- String, image의 조합으로 이루어집니다.
- 2가지 타입 중 1개 이상이 반드시 들어가야 하며, 최대 2가지 타입 모두 포함될 수 있습니다.

| 필드명   | 타입                                       | 필수여부     | 설명                                       |
| ----- | ---------------------------------------- | -------- | ---------------------------------------- |
| text  | String                                   | Optional | 사용자에게 발송될 메시지 텍스트                        |
| photo | [Photo](https://github.com/plusfriend/auto_reply/blob/master/README.md#63-photo) | Optional | 말풍선에 들어갈 이미지 정보. 1장 제한, JPEG/PNG 포맷. 개발 진행중 |

```
{
  "text": "안녕하세요.",
  "image": {
    "url": "https://hello.photo.src",
    "width": 640,
    "height": 480
  }
}
```

##### 6.2. Keyboard

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

##### 6.3. Image

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



## 7. Response Code

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



## 8. 질의응답
상단의 issue를 통해서 문의주시길 바랍니다.
- https://github.com/plusfriend/auto_reply/issues