from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello World")  # 여기서 다음 메소드로 넘어갈때 2줄을 띄우는것을 추천한다.
# 1줄 엔터
# 2줄 엔터
def select(request):  # 페이지를 여러개로 만들기위해 계속 메소드를 만드는 중이다.
    message = '수 하나를 입력해주세요.'
    return HttpResponse(message)

def result(request):
    message = '추첨 결과입니다.'
    return HttpResponse(message)
