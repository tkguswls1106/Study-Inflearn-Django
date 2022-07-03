from django.forms import ModelForm
from django import forms
from third.models import Restaurant, Review
from django.utils.translation import gettext_lazy as _

REVIEW_POINT_CHOICES = (
    ('1', 1),  # '1'은 평점 1점
    ('2', 2),  # '2'은 평점 2점
    ('3', 3),  # '3'은 평점 3점
    ('4', 4),  # '4'은 평점 4점
    ('5', 5),  # '5'은 평점 5점
)  # 평점 설정함.


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['point', 'comment', 'restaurant']
        labels = {
            'point': _('평점'),
            'comment': _('코멘트'),
        }
        widgets = {  # 장고에서 주로 사용자에게 보여주면 안되는 필드 목록들을 넣는 모델폼의 속성을 widgets로 지정하여 선언한다. widgets으로 하면 필드 속성을 직접 렌더링해와서 사용할 수 있다는 장점도 있다.
            'restaurant': forms.HiddenInput(),  # 리뷰를 달 식당 정보는 사용자에게 보여지지 않도록 한다.
            'point': forms.Select(choices=REVIEW_POINT_CHOICES)  # 평점 선택지를 인자로 전달한다.
        }  # from django import forms 선언해주고 사용하였음.
        help_texts = {
            'point': _('평점을 입력해주세요.'),
            'comment': _('코멘트를 입력해주세요.'),
        }


class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'address', 'image', 'password']
        labels = {
            'name': _('이름'),
            'address': _('주소'),
            'image': _('이미지 url'),
            'password': _('게시물 비밀번호'),
        }
        help_texts = {
            'name': _('이름을 입력해주세요.'),
            'address': _('주소를 입력해주세요.'),
            'image': _('이미지의 url을 입력해주세요.'),
            'password': _('게시물 비밀번호를 입력해주세요.'),
        }
        widgets = {
            'password': forms.PasswordInput()  # 사용자가 입력하는 값이 바로 보이지 않게 하기위해서 PasswordInput() 사용함.
                                               # 비밀번호 입력할때 가려짐.
        }
        error_messages = {
            'name': {
                'max_length': _("이름이 너무 깁니다. 30자 이하로 해주세요."),
            },
            'image': {
                'max_length': _("이미지 주소의 길이가 너무 깁니다. 500자 이하로 해주세요."),
            },
            'password': {
                'max_length': _("비밀번호가 너무 깁니다. 20자 이하로 해주세요."),
            },
        }


# 사용자가 게시물을 수정(업데이트)하고자 할때, 저장했던 패스워드와 동일한 패스워드를 입력해야하는데, 이러한 게시물 수정시 패스워드 재입력 경우에는,
# 입력폼에 다시 패스워드를 입력받아서, 새롭게 입력한 패스워드를 그걸 바로 DB에 업데이트 저장해버리면 안된다.
# 왜냐하면 class RestaurantForm(ModelForm) 은 model = Restaurant 로 인하여 모델과 연결되어있어서
# 만약 입력폼에서 틀린 패스워드를 입력해도 그대로 Restaurant 모델클래스로 연결되어 값이 업데이트 되어버리기 때문이다.
# 즉, 올바른 방법은, 패스워드가 일치하는지 우선 확인하여 검증하는 과정을 거쳐서 그것이 맞을경우에 다른 필드들을 수정하여 게시물을 수정할 수 있게 하는 것이다.
class UpdateRestaurantForm(RestaurantForm):  # 게시물 수정(업데이트) 전용의 폼클래스를 생성하였음.
    class Meta:
        model = Restaurant
        exclude = ['password']  # password는 데이터베이스에 업데이트하지 않겠다고 선언한것이다.
