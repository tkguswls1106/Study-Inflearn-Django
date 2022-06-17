from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.list, name="list"),  # 레스토랑의 리스트를 보여주는 화면이다. /third/list/ 접속 경로를 의미한다.
    path('create/', views.create, name='restaurant-create'),
    path('update/', views.update, name='restaurant-update'),
    path('detail/', views.detail, name='restaurant-detail'),
    path('delete/', views.delete, name='restaurant-delete'),
]
