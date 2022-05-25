from django.shortcuts import render
from django.http import HttpResponseRedirect

from second.models import Post
from .forms import PostForm  # views.py와 같은 second 폴더안의 forms.py 파일을 불러오므로 .forms 로 적고, forms.py 안의 PostForm 클래스를 불러온다.


# Create your views here.
def list(request):
    context = {
        'items': Post.objects.all()
    }
    return render(request, 'second/list.html', context)


def create(request):
    form = PostForm()  # 그저 forms.py 파일에 적어둔 겉의 폼 양식만 가져옴.
    return render(request, 'second/create.html', {'form':form})

def confirm(request):
    form = PostForm(request.POST)  # forms.py 파일에 적어둔 폼 양식에서 제출되어 request된 입력값을 models.py로 보냈고, 그걸 여기로 가져옴.
    if form.is_valid():  # 유효성 검사를 해준다. (예를들어 설정하였던 최대 문자열 길이를 넘기지는 않았는지 등등)
        return render(request, 'second/confirm.html', {'form': form})
    return HttpResponseRedirect('/second/create/')  # 위의 코드에서 유효성 검사에 실패했다면, 리다이렉트로 다른 사이트 주소로 접속하게 해준다.
# 처음에 create 메소드에서 값 입력받고 폼생성하고, confirm 메소드로 넘어와서 해당 값을 PostForm을 통해 form이라는 변수에 넣어주고,
# 그 변수를 유효성 검사를 하고, 유효성 검사에 통과하면 confirm.html 로 렌더링하고,
# 유효성 검사에 실패하면, 다시 입력하는 폼인 '/create/'로 리다이렉트하여 돌려보내게 된다.

