# [Django 공부 부분]

**장고 강의 영상 사이트: https://www.inflearn.com/course/django-course#curriculum**
```
{}는 {}안에 들어가있는 글자대로 예시를 적어주면된다.
//는 그 뒤에 설명을 적어주겠다.

장고란 파이썬 기반의 웹의 프레임워크이다.

프론트엔드: HTML, CSS, JS 사용
백엔드: Python 사용

dir은 디렉터리 목록을 불러온다.

<venv를 켜는 방법>
cmd 들어가기
cd first-django 입력
virtualenv venv  // venv 설치
venv\Scripts\activate 입력

<venv 켜둔 상태>
pip intall django  // 장고를 다운받아준다.
django-admin startproject {프로젝트 이름} {프로젝트가 생성될 경로}  // 현재위치경로 그대로에 프로젝트를 생성할경우에는 경로 자리에 .점만 적어주면된다.
							  // 예로써 django-admin startproject firstdjango . 를 입력하겠다.
							  // 이렇게 생성된 firstdjango 폴더는 전체 프로젝트의 코드이기때문에, 어떠한 환경변수들이나 세팅, 그리고 각종 데이터베이스의 연결에 필요한 정보들을 집어넣게 된다.
python manage.py runserver  // 프로젝트를 실행한다. cmd에 떴던, 예를들어 127.0.0.1:8000 를 인터넷 주소창에 입력하면 장고 사이트로 이동한다.

<파이참에서 venv 켜둔 상태>
python manage.py startapp first  // first-django 폴더안에 first라는 폴더와 부속파일들이 생성된다.
			      // 이제 여기 안에 우리가 필요한 코드들을 작성하고, 화면이나 실제 웹사이트의 로직 등을 구현하게 한다.
			      // 만약 에러가 나면, Windows Powershell을 관리자로 실행하고, Set-ExecutionPolicy Unrestricted 를 입력하고, y를 입력하면 에러가 안난다.

```
