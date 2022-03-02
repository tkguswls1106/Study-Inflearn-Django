from django.shortcuts import render  # 이거 덕분에 밑의 index 메소드 길이를 단축시키고 return render 시킬수 있었던 것임.
from django.http import HttpResponse

from django.template import loader
from datetime import datetime


# Create your views here.
'''
def index(request):  # 내가 이 메소드 전체를 대강 추측해서 해석해보자면,
                     # index.html에 loader로 탬플릿을 가져다놓고 context로 새로운 변수를 선언하고
                     # 그걸 렌더링으로 보내서 index.html에 적용시킨것으로 해석된다.
    template = loader.get_template('index.html')
    now = datetime.now()
    context = {
        'current_date': now
    }
    return HttpResponse(template.render(context, request))
'''  # 바로 밑의 메소드에서 같은 내용으로 길이를 단축해서 적을거라 전부 주석처리 했음.

def index(request):
    now = datetime.now()
    context = {
        'current_date': now
    }
    return render(request, 'index.html', context)  # render와 관련된 상세설명은 MD_django_study.md 에 적어놓았다.
                                                   # 여기서 다음 메소드로 넘어갈때 2줄을 띄우는것을 추천한다.
# 1줄 엔터
# 2줄 엔터
def select(request):  # 페이지를 여러개로 만들기위해 계속 메소드를 만드는 중이다.
    context = {'number':3}
    return render(request, 'select.html', context)

def result(request):
    context = {'numbers':[1,2,3,4,5,6]}
    return render(request, 'result.html', context)
