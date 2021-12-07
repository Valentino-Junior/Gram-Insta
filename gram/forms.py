from .models import Images,Comments,Profile
from django.forms import ModelForm
from django import forms

class UploadPicForm(ModelForm):
    class Meta:
        model = Images
        fields = ('image',
                  'name',
                  'caption',)

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments       
        fields=['comment']
