# from django import forms
from django.forms import ModelForm
from second.models import Post
from django.utils.translation import gettext_lazy as _  # 자세한 내용은 인프런 md 필기파일에서 확인하자.

# class PostForm(forms.Form):
#     title = forms.CharField(label = '제목', max_length=20)
#     content = forms.CharField(label = '내용', widget = forms.Textarea)  # content는 긴글을 입력해야하니 Textarea 태그를 써야한다.
#                                                                        # 하지만 만약 그냥 charField로만 써버리면, 그냥 입력박스가 나와버리기때문에,
#                                                                        # Textarea로 변환하여 사용해주기 위해서 widget이라는 옵션에 Textarea를 직접 지정해준다.

class PostForm(ModelForm):
    class Meta:
        model = Post  # 이건 models.py 파일에 있는 Post 클래스를 의미한다.
        fields = ['title', 'content']  # 그중에서 입력받고 싶은 필드(변수)는 'title', 'content'이다. 라는 뜻이다.
                                       # 이로써 models.py 파일의 변수들을 fields 라는 배열?에 넣어 꺼내서 쓰게될 수 있게 되었다.
        labels = {
            'title': _('제목'),  # from django.utils.translation import gettext_lazy as _ 때문에 _사용한 것이다. 자세한 내용은 인프런 md 필기파일에서 확인하자.
            'content': _('내용'),  # from django.utils.translation import gettext_lazy as _ 때문에 _사용한 것이다. 자세한 내용은 인프런 md 필기파일에서 확인하자.
        }
        help_texts = {
            'title': _('제목을 입력해주세요.'),
            'content': _('내용을 입력해주세요.'),
        }
        error_messages = {
            'name': {
                'max_length': _("제목이 너무 깁니다. 30자 이하로 해주세요.")
            }
        }
