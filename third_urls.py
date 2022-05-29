from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.list, name="list"),  # 레스토랑의 리스트를 보여주는 화면
]
