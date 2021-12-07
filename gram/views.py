from django.shortcuts import render,redirect
from .models import Images,Profile,Comments,Likes
from django.contrib.auth.decorators import login_required
import cloudinary
import cloudinary.uploader
import cloudinary.api
from .forms import UploadPicForm,CommentForm
from django.contrib.auth.models import User



# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    image = Images.objects.all().order_by('-id')
    if request.method == 'POST':  
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            com = form.save(commit=False)
            com.user = request.user
            com.save()
            return redirect('index')
    
    else:
        form = CommentForm()
    return render(request, 'all-glam/home.html',{'image':image,'form':form})

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
        return redirect('all-glam/home.html')
    else:
        form = UploadPicForm()
    return render(request, 'upload_pic.html', {"form": form})

@login_required(login_url='/accounts/login/')
def search_results(request):

    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        images = Images.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'all-glam/search.html',{"success":message,"images":images})

    else:
        message = "You haven't searched for any item!"
        return render(request, 'all-glam/search.html',{'warning':message})

@login_required(login_url='/accounts/login/')
def like_image(request):
    user = request.user
    if request.method == 'POST':
        image_id = request.POST.get('image_id')
        image_pic =Images.objects.get(id=image_id)
        if user in image_pic.like_count.all():
            image_pic.like_count.add(user)
        else:
            image_pic.like_count.add(user)
        like,created =Likes.objects.get_or_create(user=user, image_id=image_id)
        if not created:
            if like.value =='Like':
               like.value = 'Unlike'
        else:
               like.value = 'Like'
        like.save()
    return redirect('/')

@login_required(login_url='/accounts/login/')
def comments(request,image_id):
  form = CommentForm()
  image = Images.objects.filter(pk = image_id).first()
  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = form.save(commit = False)
      comment.user = request.user
      comment.image = image
      comment.save() 
  return redirect('index')
