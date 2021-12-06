from django.contrib import admin
from .models import Images,Likes,Comments,Profile

# Register your models here.
admin.site.register(Images)
admin.site.register(Likes)
admin.site.register(Profile)
admin.site.register(Comments)

