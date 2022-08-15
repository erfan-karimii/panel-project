from django import forms 
from captcha.fields import CaptchaField

class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=300)
    email = forms.EmailField(max_length=254)
    message = forms.CharField(widget=forms.Textarea)
    captcha = CaptchaField()
