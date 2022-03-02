# Django

### 정적 웹페이지

- 모든 사용자가 동일한 페이지를 받음

### 동적 웹페이지

- 웹페이지에 대한 요청을 받은 경우 서버는 추가적인 처리 과정 이후 클라이언트에게 응답을 보냄
- 동적 웹 페이지는 방문자와 상호작용함

### Framework

- 프로그래밍에서 특정 운영 체제를 응용 프로그램 표준 구조를 구현하는  클래스와 라이브러리 모임
- 재사용할 수 있는 수많은 코드를 프레임워크로 통합함으로써 개발자가 새로운 애플리케이션을 위한 표준 코드를 다시 작성하지 않아도 같이 사용할 수 있도록 도움
- Application framework라고도 함

###  Web Framework

- 웹 페이지를 개발하는 과정에서 겪는 어려움을 줄이는 것을 주 목적으로 데이터베이스 연동, 템플릿 형태의 표준, 세션 관리, 코드 재사용 등의 기능을 포함

### Framework Achitecture

- **MVC Design Pattern**(model - view - controller)
- 사용자 인터페이스로부터 프로그램 로직을 분리하여 애플리케이션의 시각적 요소나 이면에서 실행되는 부분을 서로 영향 없이 쉽게 고칠 수 있는 애플리케이션을 만들 수 있음
- Django는 MTV Pattern이라고 함

### MTV Pattern

- Model
  - 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리(추가, 수정, 삭제)
- Template(view)
  - 파일의 구조나 레이아웃을 정의
  - 실제 내용을 보여주는데 사용(presentation)
- View(controller)
  - HTTP 요청을 수신하고 HTTP 응답을 반환
  - Model을 통해 요청을 충족시키는데 필요한 데이터에 접근
  - template에게 응답의 서식 설정을 맡김
- 절차

  1. HTTP Request: 요청
  2. URLS(urls.py)
  3. View(views.py)
  4. HTTP Response(HTML)
  
     - Model(models.py)
  - Template(\<filename>.html)

## 장고 프로젝트 시작

### 1. 가상환경 생성
`python -m venv venv`

### 2. 가상환경 활성화
`source venv/Scripts/activate`
설치된 라이브러리 확인
`pip list`
vscode로 가서
컨트롤 쉬프트 피
python select interpreter

### 3. 장고 설치
`pip install django==3.2.12`
패키지 설치 목록 저장
`pip freeze > requirements.txt`
(git 으로 관리할 때는 venv는 올리지 않고 requirements.txt만 올려줌)

### 4. 장고 프로젝트 생성
`django-admin startproject <프로젝트명> .`
프로젝트명 -> config 하면 좀 깔끔함

### 5. 서버 켜기
`python manage.py runserver`

### 6. 앱 생성
`python manage.py startapp <어플리케이션명(복수형)>`

### 7. 앱 등록
project 내 settings.py에 INSTALLED_APPS 가장 윗줄에 추가해줘야함(*무조건 생성 후 등록!)
INSTALLED_APPS = [
'articles'
]

### 새로운 페이지 등록
urls.py에서 `from <앱명> import views`

`<앱명>/templates` 폴더 안에 html 파일 넣기

### 언어, 시간대 변경

- `settings.py`에 LANGUAGE_CODE를 'ko-kr'
- TIME_ZONE를 'Asia/Seoul'



## Django Template Language(DTL)

- 조건, 반복, 변수 치환, 필터 등의 기능을 제공

### DTL Syntax

- variable(변수)
  - render()를 사용하여 views.py에서 정의한 변수를 template 파일로 넘겨 사용하는 것
  - 변수명은 영어, 숫자와 밑줄_의 조합으로 구성될 수 있으나, 밑줄로는 시작할 수 없음
  - render() 세번째 인자로 {'key': 'value'} 넘겨줌
  - html에 {{ key }} 으로 넣어주면됨
  - key 안에 여러 key를 넣어주고 그 value가 딕셔너리라면, key.value 로 접근한다, 그 value가 리스트라면 key.index로 접근한다
- filter
  - 표시할 변수를 수정할 때 사용
  - 예시
    - {{ name|lower }}
  - [built-in filter reference](https://docs.djangoproject.com/en/4.0/ref/templates/builtins/)
- Tags
  - 출력 텍스트를 만들거나, 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행
  - 일부 태그는 시작과 종료 태그가 필요
- Comments
  - 한 줄 주석: {# 주석 작성 #}
  - 여러줄 주석: {% comment %}여기에 주석 작성{%endcomment%}

### Template inheritance(템플릿 상속)

