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
python manage.py startapp first  // first-django 폴더안에 first라는 폴더와 부속파일들이 생성된다.(first라는 웹앱 생성)
			      // 이제 여기 안에 우리가 필요한 코드들을 작성하고, 화면이나 실제 웹사이트의 로직 등을 구현하게 한다.
			      // 만약 에러가 나면, Windows Powershell을 관리자로 실행하고, Set-ExecutionPolicy Unrestricted 를 입력하고, y를 입력하면 에러가 안난다.

http://127.0.0.1:8000/ 여기서
http://127.0.0.1:8000/는 호스트나 도메인이라고 불린다.
우리는 호스트를 127.0.0.1로 설정했고, http 프로토콜에 8000번 포트로 접근하겠다 라는 뜻으로 선언한 것이다.
http://127.0.0.1:8000/ 여기 다음으로 적힐 url 부분들은 다 path라고 많이 불린다.
그래서 예를들어 path('select/', views.select, name="select") 이렇게면, http://127.0.0.1:8000/ 다음에 select/ 를 추가로 입력해주면 그에맞는 코드의 결과가 나온다.
반대로 'select/' 말고 ''처럼 아무것도 안넣고 http://127.0.0.1:8000/ 자체로도 사용이 가능하다.

보통 first 폴더안의 파이썬 파일에 코드들을 적고, 전체 프로젝트의 코드 총괄 역할인 firstdjango 폴더안의 urls.py에
include로 first 폴더안의 파이썬 파일을 참조하는 방식으로 코드를 짜주는것이
여러 웹앱들을 만들어 관리하고 사용하는 데에 훨씬 효율적이고 좋은 방식이다.

예를들어 abc.com/restaurant/1923/reviews 라는 url의 홈페이지가 있다.
그러면 이것은 1923번째(1923이라는 ID)를 가진 식당음식의 리뷰를 보여주는 url 사이트 이다.
여기서 url 사이에 껴있는 1923을 path parameter(패스 파라미터)라고 한다.
abc.com/restaurant?id=1923 이런것도 있는데, 여기서 id=1923는 ?물음표 뒤에 붙어서 쿼리 파라미터 라고 한다.

template(템플릿): 매개변수의 타입에 따라 함수나 클래스를 생성하는 메커니즘을 의미한다. 동적인 것이다.
context: 아마도 템플릿에 넣을 동적 매개변수라고 보면 될 것 같다.
render는 템플릿을 불러온다.
render의 경우 내가 가진 templates를 data를 넣어 보내고 싶을때 이용한다.
render는 django.shortcuts 패키지에 있는 함수로서 다음과 같은 파라미터를 가진다.
예를들어서 return render(request, 'index.html', context) 이면, 
첫번째 파라미터로 request를, 두번째 파라미터로 템플릿(index.html)을 받아들인다.
여기서 템플릿은 index.html으로 지정되어 있는데, 이는 templates폴더 안에 있는 index.html을 가리키게 된다.
세번째 context는 템플릿인 index.html에 전달할 데이터를 Dictionary로 전달하게 된다.

{% url 'result' %} 이런것처럼 메소드를 호출해서 출력할 수 있게하는것을 템플레이팅 이라고 한다.

block(블락): 페이지마다 반복되는 디자인과 코드 등등이 있다. 그런 html 코드들을 한곳에 모아두고 재사용할 수 있도록 도와주는 개념을 블락이라고 한다.
지정한 A.html의 블락 범위 바깥쪽 부분이 동일하게 불러와지는 방식이며, 그로 인해 다른 B.html에서 블락 범위를 지정하면 그 지정한 블락 범위 바깥쪽 부분이 A.html 블락 바깥쪽 범위 내용과 동일하게 불러와지는 것이다.
그니까 예를들어 body 태그를 제외한 부분을 블락으로 불러와서 사용할 수 있는데, 그러면 다른 html 파일에서는 body 태그 안의 내용만 코드 작성하면 된다.

block 사이에 주석을 문단으로 길게 넣으면 이상하게 에러가 난다.

```
