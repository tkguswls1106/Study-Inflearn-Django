from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from datetime import datetime


# Create your views here.
def index(request):  # 내가 이 메소드 전체를 대강 추측해서 해석해보자면,
                     # index.html에 loader로 탬플릿을 가져다놓고 context로 새로운 변수를 선언하고
                     # 그걸 렌더링으로 보내서 index.html에 적용시킨것으로 해석된다.
    template = loader.get_template('index.html')
    now = datetime.now()
    context = {
        'current_date': now
    }
    return HttpResponse(template.render(context, request))  # 여기서 다음 메소드로 넘어갈때 2줄을 띄우는것을 추천한다.
# 1줄 엔터
# 2줄 엔터
def select(request):  # 페이지를 여러개로 만들기위해 계속 메소드를 만드는 중이다.
    message = '수 하나를 입력해주세요.'
    return HttpResponse(message)

def result(request):
    message = '추첨 결과입니다.'
    return HttpResponse(message)
