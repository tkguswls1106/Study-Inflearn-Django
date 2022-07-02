from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.list, name="list"),  # 레스토랑의 리스트를 보여주는 화면이다. /third/list/ 접속 경로를 의미한다.
    path('create/', views.create, name='restaurant-create'),
    path('update/', views.update, name='restaurant-update'),
    path('delete/', views.delete, name='restaurant-delete'),
    # path('detail/', views.detail, name='restaurant-detail'),
    path('restaurant/<int:id>/', views.detail, name='restaurant-detail'),  # detail 의 주소를 패스파라미터(쿼리파라미터 말고)를 사용할 수 있도록 재정의함.
    path('restaurant/<int:restaurant_id>/review/create/', views.review_create, name='review-create'),
    path('restaurant/<int:restaurant_id>/review/delete/<int:review_id>', views.review_delete, name='review-delete'),
]
