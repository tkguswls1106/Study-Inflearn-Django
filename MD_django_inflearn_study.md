# [Django 공부 부분]

**장고 인프런 강의 영상 사이트: https://www.inflearn.com/course/django-course#curriculum**
```
{}는 {}안에 들어가있는 글자대로 예시를 적어주면된다.
//는 그 뒤에 설명을 적어주겠다.

장고란 파이썬 기반의 웹의 프레임워크이다.

프론트엔드: HTML, CSS, JS 사용
백엔드: Python 사용

dir은 디렉터리 목록을 불러온다.

장고 터미널에서 ctrl+c 키를 누르면 가동중인 프로그램(예를들어 venv)에서 나가진다.

<venv를 켜는 방법>
cmd 들어가기
cd first-django 입력
virtualenv venv  // venv 설치
venv\Scripts\activate 입력

<venv 켜둔 상태>
pip install django  // 장고를 다운받아준다.
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
render는 템플릿을 불러온다.(아마 이거 템플릿의 html파일을 불러오는건 loader이고, 템플릿에다가 다시 전달해주는게 render인것같다. 잘못 적은듯?)
render의 경우 내가 가진 templates를 data를 넣어 보내고 싶을때 이용한다.
render는 django.shortcuts 패키지에 있는 함수로서 다음과 같은 파라미터를 가진다.
예를들어서 return render(request, 'index.html', context) 이면, 
첫번째 파라미터로 request를, 두번째 파라미터로 템플릿(index.html)을 받아들인다.
여기서 템플릿은 index.html으로 지정되어 있는데, 이는 templates폴더 안에 있는 index.html을 가리키게 된다.
세번째 context는 템플릿인 index.html에 전달할 데이터를 Dictionary로 전달하게 된다.
장고 템플릿은 html 코드인데, views.py 파일 안의 메소드는 파이썬 코드로 적혀있으므로, 장고 템플릿 태그라는걸 사용한다.
템플릿 태그는 파이썬코드를 HTML로 변환해서 빠르고 쉽게 파이썬의 동적인 데이터를 사용한 웹사이트를 만들 수 있게해준다.
그래서 나중에 context 변수(딕셔너리)의 키 값을, 템플릿 디렉토리의 html 파일에서 사용할때에 {{ 키(' '는 안써도된다) }} 이런식으로
{{ }} 로 중괄호 2개를 감싸서 사용한다.
=> 장고 템플레이팅 중괄호 정리:
단, 장고 템플릿으로 html 파일에서 렌더링하는 과정에서, a태그의 url로 name값으로 변수를 넣어주거나, if 조건문이나 for while 반복문처럼 파이썬 문법의 코드를 사용할때, {% %} 이런식으로 중괄호와 %로 감싸주는 형식으로 사용한다.
그리고 마지막에 {% endfor %} 이나 {% endif %} 같은 end를 적어주어야한다.
그리고 렌더링한 변수를 그저 출력만 하고싶을때만 {{ }} 이렇게 중괄호를 두번을 써주는 것이다.
위의 a태그 렌더링 중괄호의 예를 하나 들어보자면,
<a href = "{% url 'select' %}">시작하기!</a> 가 있다.
=> loader과 render 결론:
'웹앱'의 'views.py 파일'의 '메소드'의 'loader'로, 'templates 디렉토리'의 '해당 html 파일'을 불러오고
'웹앱'의 'views.py 파일'의 '메소드'의 'render'로, 해당 메소드에서 선언한 context 변수의 값을 'templates 디렉토리'의 '해당 html 파일'로 전달하고, 그리고 '해당 html 파일'을 실행한다.
(하지만 나중에 from django.shortcuts import render 덕분에 코드 단축으로 render 안의 매개변수가 바뀌고, loader은 따로 잘 쓰지 않게 된다.)

{% url 'result' %} 이런것처럼 메소드를 호출해서 출력할 수 있게하는것을 템플레이팅 이라고 한다.

block(블락): 페이지마다 반복되는 디자인과 코드 등등이 있다. 그런 html 코드들을 한곳에 모아두고 재사용할 수 있도록 도와주는 개념을 블락이라고 한다.
지정한 A.html의 블락 범위 바깥쪽 부분이 동일하게 불러와지는 방식이며, 그로 인해 다른 B.html에서 블락 범위를 지정하면 그 지정한 블락 범위 바깥쪽 부분이 A.html 블락 바깥쪽 범위 내용과 동일하게 불러와지는 것이다.
그니까 예를들어 body 태그를 제외한 부분을 블락으로 불러와서 사용할 수 있는데, 그러면 다른 html 파일에서는 body 태그 안의 내용만 코드 작성하면 된다.

extends는 자바의 상속처럼 보면 된다.
예를들어 템플릿 디렉토리의 index.html 파일에
{% extends  'first/base.html' %} 라고 적혀있다면,
base.html 파일의
{% block content %}
{% endblock %}
이 바깥쪽 부분이 복사(상속)되어,
index.html 파일의
{% block content %}
{% endblock %}
바깥부분에 복사한부분이 붙여넣기되는 것이다.
그래서 웬만하면 base.html 파일의 {% block content %}{% endblock %} 부분은 body 태그 안에 쓰여진다.

block 사이에 주석을 문단으로 길게 넣으면 이상하게 에러가 난다.

<데이터베이스 분야 ↓>

모델은 우리가 만들 웹 서비스에서 사용할 정보의 내용, 특성을 기술하거나 정의한 것을 보통 의미한다.
우리가 웹 사이트를 만들 때 어떠한 정보들을 저장하기 위해 사용하는 개념이다.
보통은 사이트의 게시물, 댓글, 회원 정보들도 모델의 범주에 속하는데 이러한 정보를 시스템에서 처리하고 저장하기 위해 모델링이라는 과정을 거쳐야 한다.

맛집 사이트를 개발한다고 생각하고 정보를 저장하고 활용하기 위해 모델링을 하는 과정을 살펴보면,
취급할 정보의 대략적인 종류를 결정한다. 결정된 종류 각각이 모델 클래스가 된다. -> 맛집, 평가, 회원, 등
각 취급할 정보의 속성을 정리한다. -> 맛집(주소, 위치, 명칭, 전화번호, 사진 등), 평가(별점, 글쓴 시각, 글쓴 회원 등), 회원(이메일, 닉네임, 등)
각 속성의 자료형을 결정한다. -> 맛집(주소(문자열), 위치(위경도-부동소수점형), 명칭(문자열), 등)

데이터베이스는 데이터를 저장하고 관리하고 조회하기 위한 시스템을 의미한다. 당연히 우리가 웹 사이트를 만들때는 이 데이터베이스에 새로운 데이터를 저장하고 다시 이렇게 저장된 정보들을 표시한다.

장고에서는 이러한 정보 단위, 즉 모델 클래스를 파이썬 클래스를 선언하여 정의한다.
이렇게 정의한 하나의 클래스가 하나의 테이블로 만들어지고 데이터베이스는 여러 개의 테이블로 구성된다.

모델 클래스 (파이썬 클래스): 어떤 형태의 정보가 다뤄지고 저장될 지를 정의. 우리가 만들 장고 웹 앱 내에서 코드로 구현되고 웹앱이 구동되면서 실제 데이터베이스와 연동됨.
데이터베이스와 각 테이블: 실제 정의된 내용이 저장되는 장소. 웹앱과는 독립적인 시스템으로 존재함. 파이썬 기반의 장고 웹 서버가 아니라 자바 서버나 노드 서버를 통해서도 각각의 웹 앱 프레임워크가 제공하는 방식으로 모델 클래스를 정의해서 데이터베이스 서버에 접속해서 데이터를 처리하는 것이 가능. 

스키마란, (이건 인터넷에서 복사해옴)
데이터베이스의 구조(개체, 속성, 관계)와 제약 조건에 대한 정의이다. 메타 데이터라고도 한다.
데이터베이스 관리 시스템(DBMS)이 주어진 설정에 따라 데이터베이스 스키마를 생성하고,
데이터베이스 사용자가 자료를 저장, 조회, 삭제, 변경 할 때 DBMS는 자신이 생성한 데이터 베이스 스키마를 참조하여 명령을 수행한다.
한마디로 DBMS는 스키마를 참조하여 사용자의 명령을 수행하는 것이다.

<venv 켜둔 상태>
장고에서는 자동적으로 구현된 모델 클래스를 데이터베이스의 실제 테이블로 생성하는 명령어를 제공한다. ↓
python manage.py makemigrations  // 정의한 models.py에 있는 모델링 코드(모델 class)를 데이터베이스(firstdjango_settiings.py에서 정의한 DATABASE 선언에 들어가있는 ENGINE)에 맞는 형태로 코드를 정의해주는 역할을 한다.
			           // 그러면 migrations 폴더 안에 0001_initial.py 라는 파일이 생성된다. 이 안에는 models.py의 class(예를들어 POST라는 모델 스키마)와 관련되어 코드가 자동으로 생성된다. 이렇게 자동으로 만들어주는 역할을 한다.
			           // 만약 models.py 파일을 계속 수정하게되면 그때그때마다 python manage.py makemigrations를 호출하여 변화되는 코드들을 계속 0001_initial.py 파일에 업데이트 시켜줄수 있다. 데이터베이스 업데이트.
python manage.py migrate  // 이주라는 뜻이다. 코드를 실행하게되면 db.sqlite3 이라는 파일이 생성된다.(근데 나는 원래 생성되어있었음.)

<client가 server에 http 요청을 했을때의 그 흐름>
1. 예를들어 클라이언트가 서버에 abc.com 사이트에 대한 데이터를 달라는 요청을 함.
2. 장고 웹앱에서 url conf 모듈을 확인한다. (예를들어 abc.com/뒤에추가주소 이런게 있는지, path가 뭐가 있는지 등등)
3. 이 url에 맵핑된 뷰를 결정한다. (url.py 파일을 읽어들여서 여기에 정의된 내용대로 뷰 메소드를 결정하게 된다.)
4. 메소드가 실행된다. (views.py 메소드를 말한다.) 여기서 만약에 필요한 경우에는 모델을 통해서 데이터를 처리하게 된다.
5. template를 기반으로 해서 최종 html 코드를 생성하게 된다. (이는 render 함수에서 일어나게 된다.)
그렇게 마지막에 render 메소드에서 우리가 정의한 template 파일이랑 뷰 메소드의 결과값이 합쳐져서 최종 html 코드를 생성된다.
6. 생성된 최종 html 코드를 클라이언트에게 되돌려준다.

<venv 켜둔 상태>
python manage.py shell  // 장고 코드를 파일로 따로 작성하지 않아도 쉘(shell)을 이용하여 InteractiveConsole에서 장고 프레임워크를 활용한 여러가지 코드를 바로 대화형으로 실행해볼수 있다.
<shell 켜둔 상태>
from second.models import Post
post = Post.objects.create(title='this is title', content='this is content')
post  // 이거 치면 이제 <Post: Post object (1)> 이라고 뜨는데 여기서 (1)이 뭔지 이걸 설명해보자면,
        // 예를들어 학교교실에 김철수라는 학생이 10명이 있는데, 선생님이 김철수 학생을 호명하면 10명중 누구를 부르는지 명확하질않으니까 혼동되지않도록 각각 철수에게 출석번호(아이디 번호)를 붙여둔것이다.
        // 이처럼 특정 데이터를 식별할 수 있도록 id를 제공해주는것을 primary_key 라고 한다.
        // second_migrations_0001_initial.py 에서 CreatModel 부분의 'id' 부분의 primary_key (줄여서 pk) 가 있는데, 'id'라는 테이블에 있는 특정 속성은 primary_key라고 선언한 것이다. 정확하게 해당 데이터를 꺼내오기위한 아이디를 부여한 것이다.
        // 즉, <Post: Post object (1)>는 Post의 primary_key를 (1)로 지정한 것이라는 뜻이다.
post.save()  // 꼭 save를 해주어야 실제로 저장이 된다. 이제 찾아보면 db.sqlite3 파일에서 this is titlethis is content 가 적혀있는것을 확인할 수 있다.
posts = Post.objects.all()  // 메소드 호출
posts  // 입력하면 <QuerySet [<Post: Post object (1)>]> 이라고 뜬다. 이런 방식으로 나중에 계속 post = Post.objects.create(title='this is title2', content='this is content') 와 post.save() 를 계속 써주면 <QuerySet [<Post: Post object (1)>, <Post: Post object (2)>, <Post: Post object (3)> 등등 ]> 이렇게 안에 다른 목록이 더 뜨게된다.
posts[0].title  // 입력하면 'this is title' 출력됨.
posts[0].content  // 입력하면 'this is content' 출력됨.

레코드: 특정 데이터 하나를 하나의 레코드라고 부른다. 테이블은 여러 레코드의 집합이다.

사용자 웹 인터페이스를 구성하는 것 중에서 Form은 사용자의 입력을 받기 위한 필드나 위젯들이나 선택박스들의 묶음을 의미한다.
우리가 자주 보는 로그인 화면이나, 글쓰기 화면 등에 데이터를 입력 받는 입력 칸들과 버튼으로 이루어져 있다.

폼 태그와 관련해서는 웹프로그래밍 공부관련 md 파일에서 확인할 수 있다.
장고에서는 폼을 구성하기 쉽도록 프레임워크에서 지원하고 있다. 그 특징은 다음과 같다.
정의한 모델 클래스들의 모델 정보들과 연동할 수 있도록 구현해준다. (binding)
Validation 체크(입력된 정보들의 유효성 검사)를 쉽게 해준다.
악의적인 데이터(악의적인 코드)를 필터링 한다. (sanitisation) 
짧고 간결한 코드로 폼 인터페이스를 구현한다.

csrf_token 은 각각에 서로 다른 토큰을 부여하고, 토큰이 다시 서버로 제출되었을때, 유효한 요청인지 검증하기 위해 사용한다.
이는 {% csrf_token %} 이며, 아마 장고의 html파일에서 폼을 사용할때 사용되는것 같다.

return HttpResponseRedirect('/second/create/') 로, 조건에 맞는 상황이 부여되었을때(예를들어 유효성 검사),
원래 접속하려던 사이트 주소 말고 리다이렉트 하여 /second/create/ 사이트 주소로 돌려보내 접속하게 해준다.

----------------------------------------------------------------------------------------------------------------------------------------------------------
{forms.py와 models.py와 view.py와 urls.py와 html파일의 입력request값 이동 및 실행 과정 관련 내용} => 너무 길고 어려울수 있어 따로 ---점선으로 구간을 나누어 작성하였음.

혹시 몰라서 용어정리
Field = 상태, 속성, 변수
동작 = Method, 행위

아마 forms.py 파일에서 적은 코드들로 실행된 폼 인터페이스에 사용자가 입력값을 적으면, models.py 파일에 전송되어 데이터베이스로 저장이 되는것 같다.
그래서 models.py 파일의 모델 클래스(예로 Post 클래스)에 변수(예로 title, content)를 추가로 적어줄때마다, forms.py 파일에도 폼클래스(예로 PostForm 클래스)에 추가로 변수(예로 title, content)를 적어주는것이 번거롭게되니까,
아예 forms.py 파일에 from django.forms import ModelForm 를 적고, from second.models import Post 처럼, 해당 models.py 파일을 from 시키고 모델클래스인 Post를 import 해줌으로써, forms.py 파일과 models.py 파일의 클래스의 변수를 연결시켜준다.
그러면 이제 forms.py 파일에서 폼클래스를 작성할때, class PostForm(forms.Form): 를 쓰지않고, class PostForm(ModelForm): 로 모델폼을 상속받아 사용이 가능해진다.
단, 이 밑에 적을 부분은 폼클래스를 사용할때, class PostForm(ModelForm): 이 안에 반드시 작성해야하는 코드 부분이므로 규칙이라 그냥 외워두면 된다.
class PostForm(ModelForm):
    class Meta:
        model = Post  	      # 이건 models.py 파일에 있는 Post 클래스를 의미한다.
        fields = ['title', 'content']    # 그중에서 입력받고 싶은 필드(변수)는 'title', 'content'이다. 라는 뜻이다.
			      # 이로써 models.py 파일의 변수들을 fields 라는 배열?에 넣어 꺼내서 쓰게될 수 있게 되었다.
# 여기서 사이트 접속시 보여지는 이름(라벨)을 설정하려면, labels = {'title': _('제목'), } 요런식으로 정해주면 된다.

<forms.py와 models.py와 view.py와 urls.py와 html파일의 입력request값 이동 및 실행 과정>
forms.py 파일에 적어둔 폼 양식에서 제출되어 request된 입력값을 models.py로 보냈고,
그걸 models.py에서 데이터베이스에 저장하고,
그걸 view.py 파일의 특정 메소드로 가져와서 코드대로 html 파일로 다시 보내서 html 파일이 실행되면,
접속 사이트에 html 코드의 디버깅 결과물이 뜨는 것이다.

<위의 과정보다 더 자세한, 과정 서술 (주의사항은 from이랑 import 꼼꼼히 잘해주기)>
models.py 파일부터 먼저 코드 작성해주고
-> models.py 파일에 맞춰서 모델폼 클래스 연결해서 forms.py 파일 코드 작성해주고
-> views.py 파일에 '겉의 폼 양식만 가져올 용도의 메소드를 하나 작성'해주고(예를들어 def create(request):), 그 메소드 안에 변수를 하나 만들어서, 그 변수에 forms.py 파일의 클래스로 겉 폼양식 인터페이스를 가져와서 작성할 수 있게 해주는 코드를 작성한다(예를들어 form = PostForm()). 그리고 그 메소드 안에서 특정 html 파일로 해당 '겉 폼양식 인터페이스 변수'를 렌더링으로 보내주어, 렌더링한 겉 폼 양식을 해당 html 파일에서 실행하게 된다.
-> 하여튼 윗줄을 더 요약하자면 이렇게 views.py 파일에서 겉폼양식만 가져오는 def 메소드 생성해서, 메소드 안의 변수에 겉폼양식 대입해주기. 그리고 그 '겉폼양식 변수'를 특정 html로 렌더링하여 보내주면 그 html 파일 실행된다는 뜻임.
-> 그렇기에 해당 겉 폼 양식을 렌더링해 받아갈 html 코드를 작성해주어야하는데, 해당 html 파일에는 '{{ 렌더링한 겉 폼 양식의 딕셔너리의 '키' 이름 }}'과 '제출 버튼'과 '<form action="{% url 'confirm' %}" method="post"> 처럼 겉 폼양식에 무언가를 적어 제출했을때 해당 입력request값을 보내줄 또다른 url path의 name이름을 action에 지정'해주는 이 모든 요소를 갖춘 html 파일을 작성해주어야한다. (예를들어 create.html)
-> 하여튼 결국 위에서 말한 html 파일을 코드 작성하여 생성해주었고 그게 실행되었다면, 해당 html 파일(예를들어 create.html)에서 겉폼양식 출력해주고 겉폼양식에서 입력값을 입력하면, 거기서 제출버튼으로 입력된 입력request값은
-> 해당 html파일에 적혀있는 action="{% url 'url path name 작성한거' %}" 이걸로 urls.py의 특정 path를 보게되고, 거기 path에 적힌 특정 views.py 파일의 특정 메소드로 연결되어 그 메소드에 입력했었던 입력request값이 전달됨. 아마도 이 과정속에서 forms.py에 연결된 models.py의 관련 클래스의 변수에 저장되고, 이는 결국 데이터베이스에 저장될 것이라고 생각함.
-> 앞서 먼저 만들어 실행된 views.py 파일의 메소드는 겉폼양식을 가져오기만 하는거라,  '겉폼양식 변수'인 form = PostForm() 처럼 request 값은 '겉폼양식 변수'에 넣을 필요가 없었지만, 이번에 새로 연결된 views.py 파일의 메소드는 처음에 겉폼양식 html 파일에서 입력한 request 값을 이용하여 해당 입력값을 직접 이용할 새로운 html 사이트(만들어주자. 예를들어 confirm.html)에 값을 렌더링 해주어야하기때문에, 해당 메소드에는 form = PostForm(request.POST) 처럼 request 값을 가져오는 폼양식을 가져가는 변수를 만들어서 대입해주어야한다. 그리고 그 변수를 아까 말했던 새로운 html 파일에 렌더링 해준다. 그러면 해당 html 파일이 실행되는데, 그 html 파일에는 렌더링한 request변수의 value값이 직접 출력되어, 결국은 request값을 직접 화면에 출력할 수 있게 된다. 예를들어 {{ form.title.value }} 처럼 말이다.

<위의 과정을 실제 파일 이름으로 이동과정 설명 초간단 요약>
models.py 파일에 맞춰서 모델폼 클래스 연결해서 forms.py 파일 코드 작성.
-> views.py 파일의 def create(request): 메소드에서 겉폼만 second/create.html 에 렌더링해줌.
-> create.html 실행하여 겉폼양식에 입력request값 입력하여 제출함. 이제 이 입력값들고 이동함.
-> action="{% url 'confirm' %}" 이므로, url.py 파일의 path에서 name='confirm' 인거 찾음
-> 그건 views.confirm 이므로, views.py 파일의 def confirm(request): 메소드 실행.
-> 입력했었던 입력request값을 second/confirm.html 에 렌더링하여 confirm.html 실행.
-> {{ form.title.value }} 처럼 입력request값을 직접 이용하여 사이트에 출력.

<이미 파일은 모두 작성되어있다고 가정하고, 위의 과정을 실제 파일 이름만으로 더더초간단 요약>
views.py 파일의 def create(request): 메소드 실행
-> create.html 파일 실행
-> 겉폼에 입력값 입력
-> 입력request값 들고 action에 적힌 url.py로 이동
-> url.py의 path의 name='confirm'인것은 views.confirm이므로, views.py의 def confirm(request): 메소드 실행
-> confirm.html 실행
-> 결국 입력했었던 입력request값이 confirm.html 에서 직접 사용되어 사이트에 출력됨.

----------------------------------------------------------------------------------------------------------------------------------------------------------

forms.py 파일에 적힌 from django.utils.translation import gettext_lazy as _ 가 무엇인지 이 사이트에 자세히 나와있다.
=> https://def-andy.tistory.com/11
요약 설명해보자면, 
- 장고가 실행되고 기본 언어가 영어인 상태
- 영어 버전의 필드를 사용하게 됨
- 사용자가 사이트의 기본언어를 한국어로 변경
- 라벨은 여전히 영어인 상태(필드는 한 번 만 호출되기 때문에)
이러한 경우때문에 사이트가 변역되며 실제로 함수가 문자열로 변역되는동안 시간을 지연시키도록 lazy로 써주는 것이다. 아마도 lazy 뒤에는 원하는거 적으면 되는듯하다. gettext_lazy as _ 여기서는 _를 사용했다.
models.py 파일의 (fields, verbose_name, help_text, mthods short_description)
forms.py 파일의 (labels, help_text, empty_label)
apps.py 파일의 (verbose_name)
주로 이걸 사용할때 사용한다고 한다.
그래서 텍스트 앞에 'title': _('제목') 이렇게 적어준 것이다.



```
