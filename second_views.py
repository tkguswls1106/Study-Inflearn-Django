from django.shortcuts import render
from second.models import Post
from .forms import PostForm  # views.py와 같은 second 폴더안의 forms.py 파일을 불러오므로 .forms 로 적고, forms.py 안의 PostForm 클래스를 불러온다.


# Create your views here.
def list(request):
    context = {
        'items': Post.objects.all()
    }
    return render(request, 'second/list.html', context)


def create(request):
    form = PostForm()
    return render(request, 'second/create.html', {'form':form})
