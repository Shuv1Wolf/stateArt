from django import forms
from main.models import Article, News, Form
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3, ReCaptchaV2Checkbox

# class CreateArticleForm(forms.ModelForm):
#     img_title = forms.ImageField(required=False)
#     img_article = forms.ImageField(required=False)
#
#     class Meta:
#         model = Article
#         fields = [
#             'title', 'img_title', 'slug', 'title_h1',
#             'description', 'canonical', 'img_article'
#         ]
#
#         field_args = {
#             'img': {'required': False}
#         }
#
#
# class NewsForm(forms.ModelForm):
#     img = forms.ImageField(required=True, blank=True, null=True)
#
#     class Meta:
#         model = News
#         fields = [
#             'news', 'img'
#         ]
#
#         field_args = {
#             'img': {'required': True, 'blank': True, 'null': True}
#         }


class Form(forms.ModelForm):
     captcha = ReCaptchaField(widget=ReCaptchaV3)

     class Meta:
          model = Form
          fields = ['phone_number', 'time', 'name', 'captcha', 'url']

