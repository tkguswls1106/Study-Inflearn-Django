from django.shortcuts import render
from third.models import Restaurant
from django.core.paginator import Paginator

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
