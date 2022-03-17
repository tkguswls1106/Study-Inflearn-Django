from django import forms

class PostForm(forms.Form):
    title = forms.charField(label = '제목', max_length=200)
    content = forms.charFeild(label = '내용', widget = forms.Textarea)  # content는 긴글을 입력해야하니 Textarea 태그를 써야한다.
                                                                       # 하지만 만약 그냥 charField로만 써버리면, 그냥 입력박스가 나와버리기때문에,
                                                                       # Textarea로 변환하여 사용해주기 위해서 widget이라는 옵션에 Textarea를 직접 지정해준다.
