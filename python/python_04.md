# 모듈

## 모듈과 패키지

- 모듈

  > 특정 기능을 하는 코드를 파이썬 파일(.py) 단위로 작성한 것

- 패키지

  > 특정 기능과 관련된 여러 모듈의 집합
  >
  > 패키지 안에는 또 다른 서브 패키지를 포함

  ```python
  import module 
  from module import var, function, Class
  from module import *
  
  from package import module
  from package.moduel import var, function Class
  ```



## 파이썬 표준 라이브러리(Python Standard Library, PSL)

> 파이썬에 기본적으로 설치된 모듈과 내장함수

### 파이썬 패키지 관리자(pip)

> PyPI(Python Package Index)에 저장된 외부 패키지들을 설치하도록 도와주는 패키지 관리 시스템

- 패키치 설치

  - 최신 버전/ 특정 버전 /  최소 버전을 명시하여 설치 가능

    ```bash
    $ pip install SomePackage
    $ pip install SomePackage==1.0.5
    $ pip install 'SomePackage>=1.0.4'
    ```

- 패키지 삭제

  - pip는 패키지를 업그레이드 하는 경우 과거 버전을 자동으로 지워줌

    ```bash
    $ pip uninstall SomePackage
    ```

- 패키지 목록 및 특정 패키지 정보

  ```bash
  $ pip list
  $ pip show SomePackage
  ```

- 패키지 `freeze`

  - 설치된 패키지의 비슷한 목록을 만들지만, `pip install`에서 활용되는 형식으로 출력

  - 해당하는 목록은 `requirements.txt`(관습)으로 관리함

  - 아래의 명령어들을 통해 패키지 목록을 관리[1]하고 설치할 수 있음[2]

    ```bash
    $ pip freeze > requirements.txt
    $ pip install -r requirements.txt
    ```

## 가상환경

>  파이썬 표준 라이브러리가 아닌 외부 패키지와 모듈을 사용하는 경우 모두 pip를 통해 설치를 해야함 
>
> 복수의 프로젝트를 하는 경우 버전이 상이할 수 있음
>
> -> 이러한 경우 **가상환경을 만들어 프로젝트 별로 독립적인 패키지를 관리할 수 있음**

- `venv`

  - 가상환경을 만들고 관리하는데 사용되는 모듈

  - 특정 디렉토리에 가상 환경을 만들고, 고유한 파이썬 패키지 집할을 가질 수 있음

  - 예시

    ```bash
    $ python -m venv <폴더명>
    $ source <폴더명>/Scripts/activate
    
    # (venv) -> 가상환경 활성화된 상태
    
    $ deactivate 
    # 비활성화된 상태
    ```

