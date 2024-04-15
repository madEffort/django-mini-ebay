from django import forms
from django.core.validators import MaxValueValidator

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)  # 초기에 min_value를 설정

    def __init__(self, *args, max_value=100, **kwargs):  # max_value의 기본값을 예시로 100으로 설정
        super(AddToCartForm, self).__init__(*args, **kwargs)
        # max_value를 동적으로 설정
        self.fields['quantity'].validators.append(MaxValueValidator(max_value))