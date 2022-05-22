from django.shortcuts import render  # 이거 덕분에 밑의 index 메소드 길이를 단축시키고 return render 시킬수 있었던 것임.
from django.http import HttpResponse

from django.template import loader
from datetime import datetime

import random  # 로또 번호를 위해 random을 import함.


# Create your views here.
'''
def index(request):  # 내가 이 메소드 전체를 대강 추측해서 해석해보자면,
                     # index.html에 loader로 탬플릿을 가져다놓고 context로 새로운 변수를 선언하고
                     # 그걸 렌더링으로 보내서 index.html에 적용시킨것으로 해석된다.
    template = loader.get_template('index.html')
    now = datetime.now()
    context = {
        'current_date': now  # 딕셔너리 키:값. 이는 파이썬 코드인데 html 코드로 전달해주기 위해 나중에 템플릿 안의 html 파일에서 {{ corrent_date }} 이렇게 사용하여 
                             # 장고 템플릿 태그로 {{ }} 로 중괄호 2개를 감싸서 사용한다.
    }
    return HttpResponse(template.render(context, request))
'''  # 바로 밑의 메소드에서 같은 내용으로 길이를 단축해서 적을거라 전부 주석처리 했음.

def index(request):
    now = datetime.now()
    context = {
        'current_date': now
    }
    return render(request, 'first/index.html', context)  # render와 관련된 상세설명은 MD_django_study.md 에 적어놓았다.
                                                   # 여기서 다음 메소드로 넘어갈때 2줄을 띄우는것을 추천한다.
# 1줄 엔터
# 2줄 엔터
def select(request):  # 페이지를 여러개로 만들기위해 계속 메소드를 만드는 중이다.
    context = {}
    return render(request, 'first/select.html', context)

def result(request):
    chosen = int(request.GET['number'])  # GET이나 POST라는 파라미터를 통해서 전달되는 값은 string형태이므로
                                         # 숫자를 가져오기위해서는, int형으로 감싸주어야 한다.

    results = []
    if chosen >= 1 and chosen <= 45:
        results.append(chosen)

        box = []
        for i in range(0, 45):
            if chosen != i+1:  # 만약 chosen이 i+1 과 같지 않다면,
                box.append(i+1)  # 박스에 i+1 값을 집어넣어라.
                                 # 박스는 이걸보아, chosen과 중복되지 않는 수들을 걸러서 박스에 넣는 용도로 사용되는것 같다.

        random.shuffle(box)  # 박스를 셔플함.

        while len(results) < 6:
            results.append(box.pop())  # box.pop()은 box에서 랜덤으로 하나 지운 요소를 반환함.

    context = {
        'numbers':results
    }
    return render(request, 'first/result.html', context)
