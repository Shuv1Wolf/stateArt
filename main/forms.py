from django import forms
from main.models import Form
from captcha.fields import ReCaptchaField
from phonenumber_field.formfields import PhoneNumberField
from captcha.widgets import ReCaptchaV3, ReCaptchaV2Checkbox



class Form(forms.ModelForm):
     captcha = ReCaptchaField(widget=ReCaptchaV3)
     phone_number = PhoneNumberField(region="RU")
     class Meta:
          model = Form
          fields = ['phone_number', 'time', 'name', 'captcha', 'url']


