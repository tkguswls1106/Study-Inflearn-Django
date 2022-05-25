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
    if request.method == 'POST':  # form의 method가 GET인지 POST인지 검사하는 역할이다.
        form = PostForm(request.POST)  # method가 POST가 맞다면, 해당 입력받아온 데이터인 입력request값을 사용할수 있게한다.
        if form.is_valid():
            new_item = form.save()  # 이로써 입력값이 모델 스키마에 연결이 되면서 자동으로 데이터베이스에? 저장이 된다.
        return HttpResponseRedirect('/second/list/')  # 위의 코드에서 return값이 없기때문에, 유효성검사에 성공하든 실패하던간에 이 코드는 반드시 실행된다.
    form = PostForm()  # 그저 forms.py 파일에 적어둔 겉의 폼 양식만 가져옴. / 'method가 GET이라면'의 조건부분이다.
    return render(request, 'second/create.html', {'form':form})
# 그러면 과정을 설명해보자면,
# 먼저, views.py 파일의 create메소드가 단순 접속이라서 GET방식으로 실행되고, 그러면 create.html에서 겉폼양식이 뜨게되고, 거기서 입력값을 입력하고 제출하면,
# 입력한 입력request값을 들고왔기때문에 이는 POST방식으로 바뀌고, action="{% url 'create' %}" 때문에 urls.py 파일로 갔다가 views.py 파일로 와서 이번엔 create메소드를 POST방식으로 실행한다.
# 그러면, 유효성 검사를 하게되고, 유효성 검사에 성공하면 모델스키마에 연결되어 new_item = form.save()로 모델폼데이터를 저장하고 바로 '/second/list/'로 리다이렉트로 list.html 파일을 실행하게되고, 유효성 검사에 실패하면 new_item = form.save() 실행없이 바로 '/second/list/'로 리다이렉트로 list.html 파일을 실행하게된다.
# 참고로 결국 마지막에 list.html가 실행되면, 입력했던 값도 원래의 모델폼 데이터에 추가되어 list.html 안에서 출력되게 된다.

def confirm(request):
    form = PostForm(request.POST)  # forms.py 파일에 적어둔 폼 양식에서 제출되어 request된 입력값을 models.py로 보냈고, 그걸 여기로 가져옴.
    if form.is_valid():  # 유효성 검사를 해준다. (예를들어 설정하였던 최대 문자열 길이를 넘기지는 않았는지 등등)
        return render(request, 'second/confirm.html', {'form': form})
    return HttpResponseRedirect('/second/create/')  # 위의 코드에서 유효성 검사에 실패했다면, 리다이렉트로 다른 사이트 주소로 접속하게 해준다.
# 처음에 create 메소드에서 값 입력받고 폼생성하고, confirm 메소드로 넘어와서 해당 값을 PostForm을 통해 form이라는 변수에 넣어주고,
# 그 변수를 유효성 검사를 하고, 유효성 검사에 통과하면 confirm.html 로 렌더링하고,
# 유효성 검사에 실패하면, 다시 입력하는 폼인 '/create/'로 리다이렉트하여 돌려보내게 된다.

