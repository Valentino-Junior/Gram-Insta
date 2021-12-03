from django.shortcuts import render
from .models import Images
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    image = Images.objects.all().order_by('-id')
    return render(request, 'all-glam/home.html',{'image':image})


