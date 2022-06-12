from django.shortcuts import render
from third.models import Restaurant
from django.core.paginator import Paginator
from third.forms import RestaurantForm
from django.http import HttpResponseRedirect


# Create your views here.
def list(request):
    restaurants = Restaurant.objects.all()  # restaurants라는 인스턴스 변수에 할당함.
    paginator = Paginator(restaurants, 5)  # 한페이지당 5개씩 보여주겠다는 뜻이다. 참고로 Paginator는 import해서 사용해주어야한다.

    page = request.GET.get('page')  # 현재 보고있는 페이지가 어떤 페이지를 조회를 원했는지 url의 parameter(파라미터)에서 받아옴.
                                    # 예를들어 third/list?page=1 에서 1이 파라미터이다. 참고로 이건 패스 파라미터가 아니라 쿼리 파라미터이다.
    items = paginator.get_page(page)  # 쿼리 파라미터에서 페이지값을 받아서 그 페이지에 맞는 item들만 필터링해서 보여주겠다는 의미이다.
                                      # 즉, 쿼리 파라미터에서 받은 페이지값에 맞는 필드 정보들을 items 라는 변수에 넣었고, 그뿐만아니라 페이지 정보도 함께담겨간다. 그걸 렌더링 할 것이다.

    context = {
        'restaurants': items
    }
    return render(request, 'third/list.html', context)

def create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)  # 'POST' 요청으로 들어온 모든 데이터를, third_forms.py 파일의 모델폼인 RestaurantForm에 담아서 바로 데이터를 저장할 수 있다. 그리고 form이라는 변수에 저장한다.
        if form.is_valid():
            new_item = form.save()  # 이제 DB에 저장
        return HttpResponseRedirect('/third/list/')  # 유효성 검사가 성공해서 DB에 저장이 되든, 실패를해서 저장이 안되던간에, /third/list/ 경로로 리다이렉트 시킴. third_urls.py 파일의 path('list/') 부분으로 넘어가면 됨.
    form = RestaurantForm()  # 만약 request.method == 'GET' 이라면, 그저 third_forms.py 파일에 적어둔 겉의 폼 양식만 가져옴.
    return render(request, 'third/create.html', {'form': form})  # form 변수의 값을 넣은 'form'이라는 이름으로 겉폼양식을 third/create.html 파일에 렌더링 시킴.
# <과정 설명 (각 과정에 설명과 해당코드를 적어둠. 설명 부분은 앞에 @라고 적어두겠음.)>
# 1. @ third_views.py 파일의 create 메소드를 첫 실행하게 됨. 그러면 아직 POST 요청이 아닌, GET 요청임. (현재 GET 방식인 상태)
# 2. @ third_forms.py 파일의 모델폼인 RestaurantForm의 겉폼양식을 가져와서, third/create.html 로 렌더링시킴. (현재 GET 방식인 상태)
#      form = RestaurantForm()
#      return render(request, 'third/create.html', {'form': form})
# 3. @ third/create.html 실행. 그러면 렌더링해온 겉폼 양식이 띄워지는데, 거기다가 값을 입력하고 제출함. (현재 GET 방식인 상태)
# 4. @ third/create.html 파일에 적힌 <form action="{% url 'restaurant-create' %}" method="post">로 인하여 방식이 POST로 변환되며 입력값이 third_urls.py 파일의 name='restaurant-create'인 부분에 적힌 third_views.py 파일의 create 메소드로 값을 보내줌. (현재 POST 방식인 상태)
# 5. @ 그러면 third_views.py 파일의 if request.method == 'POST': 부분의 조건을 만족시키게 되고, 해당 if 조건 부분 내용 실행.
#    if request.method == 'POST':
# 6. @ POST 요청으로 들어온 모든 데이터를, third_forms.py 파일의 모델폼인 RestaurantForm의 fields 목록의 'name', 'address' 안에 입력값을 담고, 모델에 데이터를 임시 저장한다. 그리고 그렇게 저장된 모델폼 클래스인 RestaurantForm의 정보를 form이라는 변수를 선언하여 그 변수 안에 할당한다.
#      form = RestaurantForm(request.POST)
# 7. @ 그렇게 할당된 form 변수 안의 데이터에 대하여 유효성 검사(예를들어 글자수가 맞게 입력되었는지 등)를 하게됨.
#      if form.is_valid():
# 8. @ 유효성 검사에 성공하였다면, 모델폼에 임시저장하였던 fields 들의 데이터를, 할당한 form 변수를 통하여 실제로 완전히 DB에 저장시킴.
#      new_item = form.save()
# 9. @ 유효성 검사가 성공해서 DB에 저장이 되든, 실패를해서 저장이 안되던간에, /third/list/ 경로로 리다이렉트 시킴. 이는 third_urls.py 파일의 path('list/') 부분으로 넘어가면 됨. 그러면 결국은 views.list로 인하여 third_views.py 파일의 list 메소드 실행됨.
#      return HttpResponseRedirect('/third/list/')
# 10. @ 결국은 위의 과정9까지의 진행 결과로 저장된 DB를, list 메소드에서 사용하게 되는 것이다. 이처럼 라우팅을 통하여, 모델폼을 이용한 입력값을 DB에 저장하는 과정이 완료된 것이다.
# @ 즉, 밑의 4가지 파일과 urls.py 파일로 DB 저장 및 폼 라우팅이 이루어진다.
# @ models.py 파일에서는 텍스트의 유효 최대크기 같은거랑 created_at이랑 updated_at만 코드로 적어두고,
# @ forms.py 파일에서는  모델폼으로 그 겉폼틀의 코드를 작성하면 되고,
# @ views.py에서는 렌더링 코드를 작성하면 되고,
# @ html 파일에서는 <form action="{% url 'restaurant-create' %}" method="post">와 {% csrf_token %}와 <table>{{ form.as_table }}</table> 코드를 활용하여 코드를 완성하면 된다.
