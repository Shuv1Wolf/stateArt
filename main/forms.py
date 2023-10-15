from django import forms
from main.models import Article, News

class CreateArticleForm(forms.ModelForm):
    img_title = forms.ImageField(required=False)
    img_article = forms.ImageField(required=False)

    class Meta:
        model = Article
        fields = [
            'title', 'img_title', 'slug', 'title_h1',
            'description', 'canonical', 'img_article'
        ]

        field_args = {
            'img': {'required': False}
        }


class NewsForm(forms.ModelForm):
    img = forms.ImageField(required=True, blank=True, null=True)

    class Meta:
        model = News
        fields = [
            'news', 'img'
        ]

        field_args = {
            'img': {'required': True, 'blank': True, 'null': True}
        }

