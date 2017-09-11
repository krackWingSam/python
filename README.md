개인적으로 공부하는 python 내용을 기록하기 위한 repository.

 - 기본적으로 macOSx / visual studio code 환경에서 작업하며 분제가 발생하는 경우 해결방법을 이곳에 기록한다.
 - 프로젝트 생성시 python 하부 디렉토리를 만들어 작업하며 해당 목록은 숫자를 붙여 아래에 표기한다.
 - 프로젝트 단위는 최소한의 기능만을 수행하며 필요한 경우 상대경로 참조를 통해 각각의 파일을 참조한다.


1. morpheme : koNLPy 를 이용한 형태소 분석 사용법 익히기
 - 목적 한글 문장을 입력받아 형태소를 분석하기 위한 koNLPy 사용법을 익히기 위한 프로젝트
 - Komoran, Kkma, Twitter, Hannanum 클래스의 사용 예를 작성

A. vscode 환경에서 작업
 1) vscode 내부에서 python 버전을 선택하기 위해서는 아래의 작업을 수행해야 함.
   - python 3.x & pip 설치 
   - vscode interpretor 설정 : cmd + shift + p -> interpreter
   - select python 3.x
   - 필요한 라이브러리는 pip를 이용하여 설치









# 발생한 문제점들
 1. git을 이용하며 각각의 branch들을 merge 하는 경우 confilct 발생.
  - .gitignore 파일은 공통으로 사용되므로 conflict가 발생할 확률이 높음.
  - update for... 를 이용하거나 conflict가 난 부분을 삭제하고 commit, pull request 작성.
  - 이후 master 에서 수정된 사항들을 commit 할것.
  - master 에서 commit 된 부분을 update 하고 계속 사용.