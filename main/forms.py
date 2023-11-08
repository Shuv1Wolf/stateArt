import os

from django import forms
from main.models import Form
from captcha.fields import ReCaptchaField
from phonenumber_field.formfields import PhoneNumberField
from captcha.widgets import ReCaptchaV3, ReCaptchaV2Checkbox
from dotenv import load_dotenv

load_dotenv()



class Form(forms.ModelForm):
     captcha = ReCaptchaField(
          widget=ReCaptchaV3,
          public_key=os.getenv("RECAPTCHA_PUBLIC_KEY"),
          private_key=os.getenv("RECAPTCHA_SECRET_KEY"),
     )
     phone_number = PhoneNumberField(region="RU")
     class Meta:
          model = Form
          fields = ['phone_number', 'time', 'name', 'captcha', 'url']


