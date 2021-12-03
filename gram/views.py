from django.shortcuts import render
from .models import Images


# Create your views here.
def index(request):
    image = Images.objects.all().order_by('-id')
    return render(request, 'all-glam/home.html',{'image':image})
