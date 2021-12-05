from django.contrib import admin
from .models import Images,Comments,Profile

# Register your models here.
admin.site.register(Images)
admin.site.register(Profile)
admin.site.register(Comments)

