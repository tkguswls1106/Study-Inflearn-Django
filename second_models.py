from django.db import models

# Create your models here.
class Post(models.Model):  # 게시글을 남길수있는 웹앱을 만들것. 장고 모델을 상속받는 Post class를 정의.
    title = models.CharField(max_length=30)  # 모델링한 속성들을 정의. title이라는 속성은 string형이고 최대 문자열 길이는 30이다.
    content = models.TextField()  # content라는 속성도 정의. TextField는 문자열 길이를 정의하지 않는 긴 문자열을 선언할때 사용한다.

    created_at = models.DateTimeField(auto_now_add=True)  # 이 스키마를 따르는 게시물이 생성될때, 해당 이 게시글이 쓰여진 시각이 자동으로 기록됨.
    updated_at = models.DateTimeField(auto_now=True)  # 최근 수정일. 생성될때 넣을 데이터가 아니고, 수정될때마다 넣을 데이터이기때문에, _add 를 붙이지않는다.

    # num_stars = models.IntegerField()  # 예를들어 별점의 개수 보여주고싶을때 -> 숫자형 -> int -> IntegerField()
