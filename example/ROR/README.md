## 옐로아이디 챗봇 예시(Ruby on rails)

## 1. 환경

- ruby 2.3.0



## 2. 준비 사항

- [c9.io](https://c9.io/) 계정
- [카카오](https://center-pf.kakao.com/login) 계정



## 3. 참고 사이트

- [플러스 친구 관리자 센터](https://center-pf.kakao.com/login)
- [플러스 친구 자동응답 API 문서](https://github.com/plusfriend/auto_reply)



## 4. 시작하기

ChatFlow를 옐로아이디와 연동하여 서비스할 수 있는 방법을 설명합니다. 

아래 과정을 통해 고유의 클라우드 서버를 구축하고 스마트폰의 카카오톡을 이용해 테스트할 수 있습니다.

소요 시간은 약 20분입니다.

</br>

#### 4.1 C9 클라우드 서버 구축

1. **C9 로그인 후 workspace 생성 버튼 클릭**

   ![](https://ws3.sinaimg.cn/large/006tNc79gy1fl84nyqdh0j31kw0rjq7d.jpg)

   </br>

2. **Workspace 설정**

   ![](https://ws2.sinaimg.cn/large/006tNc79gy1fl84rn27t4j31kw0vcgru.jpg)

   ##### 참고 사항

   - **Clone from Git or Mercurial URL**
     - 클라우드 서버 생성 시 clone할 Repository 주소를 입력합니다
     - 여기서는 **아래의 ChatFlow git 주소를 입력**합니다.
       - https://github.com/lesimor/ChatFlow.git
   - Template은 **Ruby를 선택**합니다.
   - 입력 완료 후 아래의 **Create workspace버튼을 클릭**합니다.

   <br/>

3. **클라우드 서버의 도메인을 확인**

   ![](https://ws1.sinaimg.cn/large/006tNc79gy1fl85ainvtbj31kw0rogv8.jpg)

   ##### 참고 사항

   - c9 workspace는 생성과 동시에 고유의 도메인을 발급받습니다.
   - 해당 도메인은 추후 옐로아이디 연동 시 입력되는 주소입니다.

   </br>

4. **어플리케이션 실행**

   ![](https://ws2.sinaimg.cn/large/006tNc79gy1fl85u2fwezj31kw0rr106.jpg)

   **참고 사항**

   - 입력 명령어
     - `bundle install;rails s -p 8080 -b 0.0.0.0`
   - 1~2분 내외의 시간이 소요됩니다.

5. **동작 확인**

   ![](https://ws2.sinaimg.cn/large/006tNc79gy1fl861p54qkj31kw0vudl4.jpg)

   **참고 사항**

   - 발급받은 도메인 입력 시 위 화면이 노출되면 정상적으로 서버가 작동하는 것입니다.
   - 무료 workspace의 경우 1~2일 이내에 어플리케이션이 종료될 수 있으므로 영구적인 동작을 원할 시 비용 결제를 진행하시기 바랍니다.

   </br>

#### 4.2 카카오 옐로아이디 설정

1. **[플러스 친구 관리자 센터](https://center-pf.kakao.com/login) 접속 후 로그인(카카오톡 계정)**

   ![](https://ws3.sinaimg.cn/large/006tNc79gy1fl8igw6wkij31kw0rqgp9.jpg)

2. **새 플러스친구 만들기**

   ![](https://ws3.sinaimg.cn/large/006tNc79gy1fl8imoirvnj31kw0rttd3.jpg)

3. ㅁㄴㅇㄹㅁㄴㅇㄹㅁㄴㅇㄹ

4. ㅁㄴㄹㅇㅁㄴㅇㄹㅁㄴㅇㄹ

5. ㅁㄴㅇㄹㅁㄴㄹㄴㅁㅇㄹ

