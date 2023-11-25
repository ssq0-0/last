from django.forms import ModelForm, TextInput, Textarea
from .models import Articles, Moder


class ArticleForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['full_text']

        widgets = {
                'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите обращение'
            }),
        }


class ModerForms(ModelForm):
    class Meta:
        model = Moder
        fields = ['category_theme', 'theme', 'text']