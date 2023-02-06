from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox, ReCaptchaV3


class ContactUsForm(forms.Form):
    # name = forms.CharField(max_length=110, widget=forms.TextInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'نام ایمیل دهنده'
    # }


                                                                  # ))
    template_name = 'ContactUs/contact_form.html'
    name = forms.CharField(max_length=110, required=True, error_messages={'required': 'این فیلد باید پر شود'})
    subject = forms.CharField(max_length=110)
    email = forms.EmailField(error_messages={'invalid': 'ایمیل اشتباه است دوست من '})
    text = forms.CharField(widget=forms.Textarea(), max_length=500)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox(
        api_params={'hl': 'fa'}
    ))

    # captcha = ReCaptchaField(widget=ReCaptchaV3(),
    #     public_key='76wtgdfsjhsydt7r5FFGFhgsdfytd656sad75fgh',
    #     private_key='98dfg6df7g56df6gdfgdfg65JHJH656565GFGFGs',
    # )