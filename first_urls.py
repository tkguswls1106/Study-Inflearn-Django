from django.urls import path

from . import views  # 어차피 현재위치인 first 안의 views.py 파일을 갖고 오는것이기 때문에
                     # first 말고 . 로 대체하여 적어도 된다.

urlpatterns = [
    path('', views.index, name = 'index')  # import한 first안의 views.py 파일의 index 함수를 불러온다.
                                           # path 첫번째에 ''로 아무것도 안넣어줬으니, 이건 루트 path 라고 부른다.
]
