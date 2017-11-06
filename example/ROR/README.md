## 플러스친구 EchoBot 예시(Ruby on rails)

사용자가 입력한 텍스트를 그대로 따라하는 EchoBot 예시입니다.

플러스친구와 연동하여 서비스할 수 있는 방법을 설명합니다. 

아래 과정을 통해 고유의 클라우드 서버를 구축하고 스마트폰의 카카오톡을 이용해 테스트할 수 있습니다.

소요 시간은 약 20분입니다.

</br>

## 1. 환경

- ruby 2.3.0



## 2. 준비 사항

- [c9.io](https://c9.io/) 계정
- [카카오](https://center-pf.kakao.com/login) 계정



## 3. 참고 사이트

- [플러스 친구 관리자 센터](https://center-pf.kakao.com/login)
- [플러스 친구 자동응답 API 문서](https://github.com/plusfriend/auto_reply)



## 4. 시작하기

#### 4.1 C9 클라우드 서버 구축

c9이 제공하는 클라우드 서버 서비스를 통해 별도의 개발환경 설정 및 번거로운 구축 과정 없이 **무료로 임시 개인 서버**를 생성할 수 있습니다.

아래의 내용은 어디서나 접근 가능한 클라우드 서버를 구축하고 **Ruby on rails 애플리케이션을 옐로아이디와 연동하기 위한 사전 준비 과정**을 설명합니다.

</br>

##### 4.1.1 [C9 로그인](https://c9.io/) 후 workspace 생성 버튼 클릭

![](https://ws3.sinaimg.cn/large/006tNc79gy1fl84nyqdh0j31kw0rjq7d.jpg)

</br>

##### 4.1.2 Workspace 설정

![](https://ws1.sinaimg.cn/large/006tNc79gy1fl8it67fukj31kw0vc7bh.jpg)

##### 참고 사항

- **Clone from Git or Mercurial URL**
  - 클라우드 서버 생성 시 clone할 Repository 주소를 입력합니다
  - 여기서는 **아래의 ChatFlow git 주소를 입력**합니다.
    - https://github.com/lesimor/ChatFlow.git
- Template은 **Ruby를 선택**합니다.
- 입력 완료 후 아래의 **Create workspace버튼을 클릭**합니다.

<br/>

##### 4.1.3 클라우드 서버의 도메인을 확인

![](https://ws3.sinaimg.cn/large/006tNc79gy1fl8ipbz9ovj31kw0rogv8.jpg)

##### 참고 사항

- c9 workspace는 생성과 동시에 **고유의 주소**를 발급받습니다.
- 해당 URL은 추후 **옐로아이디 연동 시 입력되는 주소**입니다.

</br>

##### 4.1.4 어플리케이션 실행

![](https://ws4.sinaimg.cn/large/006tKfTcgy1fl8stys87yj31kw0rlqau.jpg)

**진행 순서**

1. **bash창**으로 이동합니다.

2. bash의 현재 경로를 **Ruby on rails 디렉토리로 변경**합니다.

   `cd /example/ROR` 입력

3. **Gem을 설치**합니다.

   `bundle install` 입력(**최초 서버 실행 또는 Gem 변동사항이 있는 경우에만**)

   (1~2분 내외의 시간이 소요됩니다.)

4. **서버를 실행**합니다.

   `rails s -p 8080 -b 0.0.0.0` 입력

</br>

##### 4.1.5 동작 확인

![](https://ws2.sinaimg.cn/large/006tNc79gy1fl861p54qkj31kw0vudl4.jpg)

**참고 사항**

- 발급받은 도메인 입력 시 위 **화면이 노출되면 정상적으로 서버가 작동**하는 것입니다.
- 무료 workspace의 경우 1~2일 이내에 웹서버가 꺼질 수 있으므로 영구적인 동작을 원할 시 비용 결제를 진행하시기 바랍니다.
  - 서버 재실행 방법
    - 해당 workspace의 bash창에서 `cd /example/ROR;rails s -p 8080 -b 0.0.0.0`  입력

</br>

#### 4.2 카카오 옐로아이디 설정

플러스 친구 관리자 센터를 통해 **챗봇을 생성**하고 위에서 구축한 C9 workspace와 연동하는 과정을 설명합니다.

과정을 마치고 나면, **전세계의 모든 카카오톡 유저가 사용가능한 챗봇**을 런칭할 수 있게 됩니다.

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

</br>

##### 4.2.6 공개설정하기

1. asdfasdfasfdasf

