from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class CommentForm(forms.Form):
    name = forms.CharField(max_length=140)
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'متن پیام'}))
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(api_params={'hl': 'fa'}))
