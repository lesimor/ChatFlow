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

</br>

#### 3.3. API 클라이언트 테스트
챗봇 시나리오를 생성하면 개발 서버에서 직접 ChatFlow API를 실행할 수 있습니다.

카카오 옐로아이디 / 네이버 톡톡친구 뿐만 아니라 각종 웹/어플리케이션 개발 시에도 범용적으로 사용 가능합니다.

관리자 페이지에서도 테스트를 실행할 수 있습니다.

 - 특정 챗봇 시나리오의 유저가 5분 이내로 메시지를 보내지 않는 경우 해당 유저의 챗봇 시나리오는 entry node부터 다시 시작합니다.

</br>

## 4. 용어 설명

#### 4.1. ChatFlow API
- ChatFlow 이용자가 특정 시나리오 상의 유저 상태를 제어하는 API입니다.
- http(s) restful api를 통하여 개발 서버 -> ChatFlow 서버를 호출합니다.

#### 4.2. developer_id

- ChatFlow에서 회원가입 시 개발자 계정에 발급되는 고유 ID 값입니다.
- 개발자를 식별하기 위해 ChatFlow API 호출 시 매번 포함해야 하는 값입니다.


#### 4.3. app_id
- 개발자의 챗봇 시나리오를 식별할 수 있는 고유 ID 값입니다.
- developer_id와 함께 ChatFlow API 호출 시 함께 포함해야 하는 값입니다.

#### 4.4. user\_id
- 개발자 챗봇 시나리오 내의 사용자를 식별하기 위한 값입니다.
- 개발사 서버에서는 API 호출 시 각 사용자의 고유 키를 함께 전달해주어야 합니다.
- user\_id는 각각의 서비스 이용자에 대해 발급된 고유한 값이어야 합니다.


</br>

## 5. API specifications

- 개발사 서버에서 ChatFlow 서버를 호출하는 API에 대한 명세서입니다.


#### 5.1. 시나리오 상의 유저 상태 전이 API
- 개발사의 애플리케이션 사용자가 입력한 메시지를 ChatFlow 서버로 전달하는 API입니다.

##### Specification
- **Method** : POST
- **URL** : https://chatflow.kr/api/v1/message
- **Content-Type** : application/json; charset=utf-8
- **Parameters**

| 필드명          | 타입     | 필수여부     | 설명                             |
| ------------ | ------ | -------- | ------------------------------ |
| developer_id | String | Required | **개발자 식별 ID**                  |
| app_id       | String | Required | 개발자의 챗봇 **시나리오 식별 ID**         |
| user_id      | String | Required | 개발자 애플리케이션 내의 **사용자 식별 ID**    |
| message      | String | Required | 개발자 애플리케이션 내의 **사용자가 입력한 메시지** |
- **예제**
```
curl -XPOST 'https://chatflow.kr/api/v1/message' -d '{
  "developer_id": "issuedDeveloperID",
  "app_id": "issuedApplicationID",
  "user_id": "uniqueUserIDofService",
  "message": "톨 사이즈 아메리카노로 주문할게요."
}'
```
- **Response**

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
	"action": "slot",
	"message": {
		"text": "주소를 알려주세요.",
		"image": null
	},
	"keyboard": {
		"type": "text"
	},
	"slot": {
		"$drink": "아메리카노",
		"$size": "톨"
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

#### 5.2. 유저 상태 초기화

- 서비스되는 애플리케이션에서 예외 상황이 발생한 경우 유저의 상태를 시나리오 상의 entry로 전이하는 API입니다.

##### Specification
- **Method** : GET
- **URL** : https://chatflow.kr/api/vi/reset
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

</br>

#### 5.3. 특정 노드로 상태 전이

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

</br>

