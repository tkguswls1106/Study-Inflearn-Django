from django.urls import path

from . import views  # 어차피 현재위치인 first 안의 views.py 파일을 갖고 오는것이기 때문에
                     # first 말고 . 로 대체하여 적어도 된다.

urlpatterns = [
    path('', views.index, name="index"),  # import한 views.py 파일 안의 index 함수를 불러온다.
                                          # 이건그저 단순히 path로 index 메소드를 연결해준것 뿐이니까, ''로 적어준다.
                                          # 그니까 http://127.0.0.1:8000/ 이거 뒤에 아무것도 안붙여준다.
                                          # path 첫번째에 ''로 아무것도 안넣어줬으니, 이건 루트 path 라고 부른다.
    path('select/', views.select, name="select"),  # http://127.0.0.1:8000/ 뒤에 select/ 를 적으면 그에맞는 코드의 결과가 나온다.
    path('result/', views.result, name="result")  # http://127.0.0.1:8000/ 뒤에 result/ 를 적으면 그에맞는 코드의 결과가 나온다.
]
