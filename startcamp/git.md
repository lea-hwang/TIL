# Git

## git의 기본적인 구조

![git image](git.assets/git.png)

working directory : 현재 작업 공간

staging area: 

local repository: 

### 명령어

`git init`:해당 폴더를 git으로 관리 시작 

`git status`: 현재 working directory 및 staging area의 상태

`git config --global user.email {이메일}` : 이메일 등록

`git config --global user.name {이름}` : 이름 등록

`git add {파일 및 폴더명}` : working directory에서 staging area로 올리기

`git add .` : 현재 working directory의 모든 파일을 올리기

`git commit`: staging area에서 local repository로 올리기

`git commit -m '{메세지 내용}'`: 메모를 작성할 수 있음

`git log`: commit 내용을 보여줌



- untracked : staging area에 올라가 있지 않은 파일 및 폴더

- tracked : staging area에 이미 올라간 적이 있는 파일 및 폴더

