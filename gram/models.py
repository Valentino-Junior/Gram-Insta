from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here
class Images(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=50)
    caption = models.TextField(max_length=2000)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.image