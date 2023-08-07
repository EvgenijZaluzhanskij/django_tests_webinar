from django import forms

from .models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('id', 'title', 'text', 'author', 'created_at')
