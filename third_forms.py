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
        fields = ['name', 'address']
        labels = {
            'name': _('이름'),
            'address': _('주소'),
        }
        help_texts = {
            'name': _('이름을 입력해주세요.'),
            'address': _('주소를 입력해주세요.'),
        }
        error_messages = {
            'name': {
                'max_length': _("이름이 너무 깁니다. 30자 이하로 해주세요."),
            }
        }
