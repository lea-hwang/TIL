# 모듈

## 모듈과 패키지 불러오기

```python
import module 
from module import var, function, Class
from module import *

from package import module
from package.moduel import var, function Class
```



## 파이썬 표준 라이브러리(Python Standard Library)

> 파이썬에 기본적으로 설치된 모듈과 내장함수

### 파이썬 패키지 관리자(pip) 명령어

- 패키치 설치

  - 최신 버전/ 특정 버전 /  최소 버전을 명시하여 설치 가능

    ```bash
    $ pip install SomePackage
    $ pip install SomePackage == 1.0
    $ pip install SomePackage >= 1.0
    ```

- 패키지 정보

  

  ```bash
  $ pip list pip show Somepackage
  ```

- 패키지 `freeze`

  - 설치된 패키지의 비슷한 목록을 만들지만, `pip install`에서 활용되는 형식으로 출력

  - 해당하는 목록은 `requirements.txt`(관습)으로 관리함

    ```bash
    $ pip freeze > requirements.txt
    $ pip install -r requirements.txt
    ```



## 사용자 모듈과 패키지

### 모듈/ 패키지 활용하기



## 가상환경

```bash
$ python -m venv <폴더명>
$ source <폴더명>/Scripts/activate

# (venv) -> 가상환경 활성화된 상태

$ deactivate 
# 비활성화된 상태
```



