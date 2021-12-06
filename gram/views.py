from django.shortcuts import render,redirect
from .models import Images,Profile,Comments
from django.contrib.auth.decorators import login_required
import cloudinary
import cloudinary.uploader
import cloudinary.api
from .forms import UploadPicForm



# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    image = Images.objects.all().order_by('-id')
    return render(request, 'all-glam/home.html',{'image':image})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    pics = Images.objects.filter(user_id=current_user.id)
    profile = Profile.objects.filter(user_id=current_user.id).first()
    return render(request, 'all-glam/home.html', {"pics": pics, "profile": profile})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    pics = Images.objects.filter(user_id=current_user.id)
    profile = Profile.objects.filter(user_id=current_user.id).first()
    return render(request, 'profile.html', {"pics": pics, "profile": profile})

@login_required(login_url='/accounts/login/')
def upload_pic(request):
    current_user = request.user
    profile = Profile.objects.get(user = current_user)
    if request.method == "POST":
        form = UploadPicForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.save()
        return redirect('/')
    else:
        form = UploadPicForm()
    return render(request, 'upload_pic.html', {"form": form})

def search_results(request):

    if 'images' in request.GET and request.GET["images"]:
        search_term = request.GET.get("images")
        images = Images.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'all-glam/search.html',{"message":message,"images":images})

    else:
        message = "Does not exist"
        return render(request, 'all-glam/search.html',{'warning':message})
