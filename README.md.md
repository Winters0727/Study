# Git

- **SCM** (What?) : Source Code Management (소스 코드 관리 도구)

- **VCS** (How?) : Version Control System (버전을 기반으로 관리)
  - Folder-based



**Git 참고 문서** : https://backlog.com/git-tutorial/kr/intro/intro1_1.html



# How to use Git?

### Git bash

``````shell
$ git --version # git 버전 및 설치 유무 확인
$ git init # git 실행
$ git status # 폴더의 현재 상태 출력
$ git add (file_name or folder_name) # 파일 추가
$ git commit # commit, 로그인이 필요(meta data)
$ git config --global user.email "email address" # 메타데이터 등록
$ git config --global user.name "name" # 메타데이터 등록
$ git config --global --list # 전역 설정 확인
$ git commit -m "commit message" # commit 메세지 작성 (항상 적성해야함!)
$ git log # 로그 확인
$ git log --oneline # 로그 확인 시 메세지 한줄만 출력
$ git checkout hexadecimal(16진수) # 해당 commit 시점으로 돌아감
$ git checkout master # 최근 commit 시점으로 돌아감
$ git remote # 원격 저장소 커맨드
$ git remote add (저장소의 이름,별명) (저장소의 주소) # 원격 저장소 추가
$ git remote -v # -v : verbose 모드, 정보를 자세히 출력
$ git push (저장소의 이름) (branch의 이름) # 로컬 저장소에서 원격 저장소로 파일을 보냄
$ git add -u # 변경된 사항 모두를 반영
$ git clone (저장소의 주소) (저장소의 새이름) # 원격저장소 복사
$ git pull (저장소의 이름,별명) (저장소의 주소) # 원격 저장소의 변경된 정보 가져오기
``````



### Shell commad

``````shell
$ mkdir TIL # 폴더 생성
$ cd TIL # 폴더로 이동
$ touch file_name # 파일 생성
$ cp (복사할 파일의 주소) (복사할 장소) # 파일 복사
$ ls # 파일 리스트
$ ls -a # 모든 파일 리스트 (숨김 폴더 포함)
$ cd .git
$ cat confing # 정보 출력
$ rm -r .git/ # 파일 제거
``````