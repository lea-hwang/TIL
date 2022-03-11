# Git

## branch

- `git branch`: 브랜치 목록 확인 
- `git branch <브랜치이름>` :새로운 브랜치 생성
- `git branch -d <브랜치이름>`: 특정 브랜치 삭제
- `git switch <브랜치이름>`: 다른 브랜치로 이동
- `git log --oneline --all` : 모든 브랜치의 로그 확인
- `git log --oneline --all --graph`: 갈라진 모양 볼 수 있음
- `git branch -d <브랜치 이름>`: 병합된 프랜치만 삭제
- `git branch -D <브랜치 이름>`: 강제 삭제
- `git switch -c <브랜치 이름>`: 브랜치를 새로 생성과 동시에 이동

​	*** 모든 파일들이 깃으로 버전관리 받고 있는지 확인하고 다른 브랜치로 이동해야함

## merge

- `git merge 병합할 브랜치 이름`: merge 하기 전에 합치려고 하는 브랜치, 즉 메인 브랜치로 switch해야함
- 