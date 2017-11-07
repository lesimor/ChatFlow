## 플러스친구 EchoBot 예시(Flask)

사용자가 입력한 텍스트를 그대로 다시 응답하는 EchoBot 예시입니다.

아래 과정을 통해 **개발용 클라우드 서버를 구축**하고 **국내의 모든 카카오톡 유저가 사용할 수 있는 챗봇 서비스를 런칭**할 수 있습니다.

소요 시간은 **약 10분**입니다.

</br>

## 1. 환경 설정

- 무료로 제공되는 클라우드 서버를 이용하기 때문에 **별도의 환경 설정은 필요하지 않습니다.**


</br>


## 2. 준비 사항

- [c9.io](https://c9.io/) 계정
- [카카오](https://center-pf.kakao.com/login) 계정


</br>


## 3. 참고 사이트

- [플러스 친구 관리자 센터](https://center-pf.kakao.com/login)
- [플러스 친구 자동응답 API 문서](https://github.com/plusfriend/auto_reply)


</br>


## 4. 시작하기

#### 4.1 C9 클라우드 서버 구축

c9이 제공하는 클라우드 서버 서비스를 통해 별도의 개발환경 설정 및 번거로운 구축 과정 없이 **무료로 개발용 서버**를 생성할 수 있습니다.

아래의 내용은 챗봇 서비스를 제공하는 클라우드 서버를 구축하고 **Flask 애플리케이션을 옐로아이디와 연동하기 위한 사전 준비 과정**을 설명합니다.

</br>

##### 4.1.1 [C9 로그인](https://c9.io/) 후 workspace 생성 버튼 클릭

![](https://ws3.sinaimg.cn/large/006tNc79gy1fl84nyqdh0j31kw0rjq7d.jpg)

</br>

##### 4.1.2 Workspace 설정

![](https://ws3.sinaimg.cn/large/006tKfTcgy1fl9gmuqmz1j31kw0rz46i.jpg)

##### 참고 사항

- **Clone from Git or Mercurial URL**
  - 클라우드 서버 생성 시 clone할 Repository 주소를 입력합니다
  - 여기서는 **아래의 ChatFlow git 주소를 입력**합니다.
    - https://github.com/lesimor/ChatFlow.git
- Template은 **Python를 선택**합니다.
- 입력 완료 후 아래의 **Create workspace버튼을 클릭**합니다.

<br/>

##### 4.1.3 클라우드 서버의 호스트명을 확인

![](https://ws1.sinaimg.cn/large/006tKfTcgy1fl9g8vt9tcj31kw0rqdng.jpg)

##### 참고 사항

- 해당 호스트명은 **옐로아이디 연동 시 입력되는 주소**입니다.

</br>

##### 4.1.4 패키지 설치 및 서버 실행

![](https://ws3.sinaimg.cn/large/006tKfTcgy1fl9gohdmquj31kw0rtdo6.jpg)

##### 진행 순서

1. **bash창**으로 이동합니다.

2. bash의 현재 경로를 **Flask 프로젝트 디렉토리로 변경**합니다.

   `cd /example/flask` 입력

3. **패키치를 설치**합니다.

   `sudo pip install -r requirements.txt` 입력

4. **서버를 실행**합니다.

   `python run.py` 입력

</br>

##### 4.1.5 동작 확인

![](https://ws1.sinaimg.cn/large/006tKfTcgy1fl990lkjekj31kw0vudl4.jpg)

**참고 사항**

- 발급받은 호스트명 입력 시 위 **화면이 노출되면 정상적으로 서버가 작동**하는 것입니다.
- 개발용 서버이기 때문에 1~2일 이내에 서버가 꺼집니다.([참조](https://community.c9.io/t/how-do-i-figure-out-the-url-of-my-cloud9-project/12966/2))
  - 서버 재실행 방법
    1. bash에서 flask 프로젝트 경로 이동
    2.  `python run.py`  입력

</br>

#### 4.2 카카오 옐로아이디 설정

플러스 친구 관리자 센터를 통해 **챗봇을 생성**하고 위에서 구축한 C9 workspace와 연동하는 과정을 설명합니다.

과정을 마치고 나면, **국내 모든 카카오톡 유저가 사용가능한 챗봇**을 런칭할 수 있게 됩니다.

</br>

##### 4.2.1 [플러스 친구 관리자 센터](https://center-pf.kakao.com/login) 접속 후 로그인(카카오톡 계정)

![](https://ws3.sinaimg.cn/large/006tNc79gy1fl8igw6wkij31kw0rqgp9.jpg)

</br>

##### 4.2.2 새 플러스친구 만들기 버튼 클릭 

![](https://ws3.sinaimg.cn/large/006tNc79gy1fl8imoirvnj31kw0rttd3.jpg)

</br>

##### 4.2.3 플러스친구 정보 입력 및 생성

![](https://ws4.sinaimg.cn/large/006tKfTcgy1fl8t916kd8j31kw0rmdm2.jpg)

</br>

##### 4.2.4 API형 설정하기 클릭

![](https://ws2.sinaimg.cn/large/006tNc79gy1fl8jb4xw3kj31kw0rhagz.jpg)

</br>

##### 4.2.5 앱 등록하기

![](https://ws2.sinaimg.cn/large/006tNc79gy1fl8qk29cdij31kw0rt7dw.jpg)

##### 참고 사항

- **앱 URL**: [Step 4.1.3](https://github.com/lesimor/ChatFlow/tree/kakao-echobot/example/flask#413-클라우드-서버의-호스트명을-확인)에서 확인한 호스트명 입력
  - API 테스트 후 위 스크린샷 처럼 뜨면 정상적으로 동작하는 것입니다.

</br>

##### 4.2.6 공개설정하기

![](https://ws4.sinaimg.cn/large/006tKfTcgy1fl97c6wj7ij31kw0r8n5t.jpg)

</br>

#### 4.3 카카오톡 앱을 통한 동작확인

##### 4.3.1 플러스친구 검색

![](https://ws3.sinaimg.cn/large/006tKfTcgy1fl97xso7urj314a0yqq7p.jpg)

</br>

##### 4.3.2 EchoBot 테스트

![](https://ws4.sinaimg.cn/large/006tKfTcgy1fl984b4spaj30ku11241v.jpg)

</br>

## 5. 마무리

위 예제는 옐로아이디 챗봇을 개발하기 위한 기초를 제공합니다.

이제부터는 각자 workspace 내의 코드를 수정하면서 자신만의 챗봇을 개발해보시기 바랍니다.

C9 클라우드 서버는 개발용 서버이며 실제 서비스는 별도의 서버에서 진행해주세요.

감사합니다.

