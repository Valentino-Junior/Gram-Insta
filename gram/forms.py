from .models import Images,Comments,Profile
from django.forms import ModelForm

class UploadPicForm(ModelForm):
    class Meta:
        model = Images
        fields = ('image',
                  'name',
                  'caption',)