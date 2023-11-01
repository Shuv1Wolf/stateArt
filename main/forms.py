from django import forms
from main.models import Article, News, Form
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3, ReCaptchaV2Checkbox



class Form(forms.ModelForm):
     captcha = ReCaptchaField(widget=ReCaptchaV3)

     class Meta:
          model = Form
          fields = ['phone_number', 'time', 'name', 'captcha', 'url']

