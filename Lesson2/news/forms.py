from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInputa, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anond', 'full_text', 'date']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            "date": DateTimeInputa(attrs={
                'class': 'form-control',
                'placeholde': 'Дата публикации'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),
        }