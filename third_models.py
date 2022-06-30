from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)  # 이 스키마를 따르는 게시물이 생성될때, 해당 이 게시글이 쓰여진 시각이 자동으로 기록됨.
    updated_at = models.DateTimeField(auto_now=True)  # 최근 수정일. 생성될때 넣을 데이터가 아니고, 수정될때마다 넣을 데이터이기때문에, _add 를 붙이지않는다.

class Review(models.Model):
    point = models.IntegerField()
    comment = models.CharField(max_length = 500)

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)  # Restaurant 모델클래스의 ForeignKey 를 갖고온다.
    # 위의 모델클래스를 class Restaurant 와의 릴레이션 정의.
    # Many-to-one 관계로써, many는 모델클래스 Review이고, one은 모델클래스 Restaurant 이다.

    # ForeignKey 는 외래키로써, 외부에서 온 키를 의미하고, 이는 모델클래스 Restaurant 의 primary key ( = pk id 값 1 ~) 를 의미한다.
    # 만약에 Restaurant 를 하나 처음으로 하나 등록하면 그 pk값은 1이 될테고, 그 레스토랑의 리뷰다 함은 ForeignKey 는 1이 되는것이다.
    # 즉, 각 레스토랑마다 각각의 리뷰들을 적용해주는 것으로써,
    # 현재 보고 있는 리뷰 데이터가 어느 레스토랑(식당)을 가리키고 있는지 지정하기위한 속성이 restaurant 인것이다.

    # 만약에 특정 식당이 삭제되면 그 해당 식당의 리뷰들은 없는 식당을 참조하게되는거니까, 이경우에는 상황을 어떻게 처리할지를 물어보는 의미로써, on_delete=models.CASCADE 를 적어줌으로써, 식당이 삭제되면 리뷰들도 같이 삭제되게 한다. (정확히 말하면 식당을 가리키는 리뷰의 pk값을 삭제함으로써, 결과적으로 리뷰를 삭제하게 되는것이다.)
    # on_delete=models.CASCADE 의 의미를 풀어서 자세히 설명하자면, 
    # on_delete 라는 속성은, restaurant가 바라보고 있는 모델클래스인 Restaurant의 데이터가 삭제되었을때, 판단을 어떻게 처리할것인가? 라는 의미이고,
    # models.CASCADE 의 의미는, 참조한 오브젝트(models인 모델클래스 Restaurant)가 삭제되면, 이를 똑같이 따라서(CASCADE) 해당 오브젝트를 참조한 오브젝트인 restaurant도 함께 삭제하라는 의미이다.

    # 만약에 CASCADE가 아닌, SET_NULL이 들어가서 on_delete=models.SET_NULL 라는 코드였다고 가정한다면,
    # 이는 특정 식당이 삭제되면, 그 식당에 해당하는 리뷰의 restaurant(= 해당 식당의 리뷰의 pk id값)을 NULL값으로 바꿔줌으로써, 리뷰를 삭제하는것이 아닌, 리뷰가 가리키는 식당이 없도록 만들어줌으로써, 식당만 삭제하고 그저 리뷰는 가리키는 곳이 없도록 설정해준 것이다.

    created_at = models.DateTimeField(auto_now_add=True)  # 리뷰 작성 시 (이 모델의 데이터(레코드) 저장 시) 생성 시각
    updated_at = models.DateTimeField(auto_now=True)

    # 여기까지 models.py 파일의 Review 모델클래스를 작성을 완료하였다면,
    # 항상 models.py 파일을 바꿀때마다 반드시 해줘야하는 python3 manage.py makemigrations 와 python3 manage.py migrate 를 해주어야한다.
    # 다 완료했다면, db.sqlite3 파일에 들어가보면 restaurant가 restaurant_id 라는 이름의 속성으로 db에 자동 저장된것을 확인할 수 있다.
