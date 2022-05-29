from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)  # 이 스키마를 따르는 게시물이 생성될때, 해당 이 게시글이 쓰여진 시각이 자동으로 기록됨.
    updated_at = models.DateTimeField(auto_now=True)  # 최근 수정일. 생성될때 넣을 데이터가 아니고, 수정될때마다 넣을 데이터이기때문에, _add 를 붙이지않는다.
