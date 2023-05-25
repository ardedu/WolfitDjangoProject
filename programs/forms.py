from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'description', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Titre'
            }),
            "description": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Description'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'La Date'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Contenu'
            }),
        }
