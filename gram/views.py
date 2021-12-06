from django.shortcuts import render,redirect
from .models import Images,Profile,Comments,Likes
from django.contrib.auth.decorators import login_required
import cloudinary
import cloudinary.uploader
import cloudinary.api
from .forms import UploadPicForm
from django.contrib.auth.models import User



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
        return redirect('all-glam/home.html')
    else:
        form = UploadPicForm()
    return render(request, 'upload_pic.html', {"form": form})

def search_results(request):

    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        images = Images.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'all-glam/search.html',{"success":message,"images":images})

    else:
        message = "You haven't searched for any item!"
        return render(request, 'all-glam/search.html',{'warning':message})

def like_image(request):
    user = request.user
    if request.method == 'POST':
        image_id = request.POST.get('image_id')
        image_pic =Images.objects.get(id=image_id)
        if user in image_pic.likes_count.all():
            image_pic.likes_count.add(user)
        else:
            image_pic.likes_count.add(user)    
            
        like,created =Likes.objects.get_or_create(user=user, image_id=image_id)
        if not created:
            if like.value =='Like':
               like.value = 'Unlike'
        else:
               like.value = 'Like'

        like.save()       
    return redirect('/')
# def likes(request,id):
#     user_like = Likes.objects.filter(image_id=id).first()
#     if Likes.objects.filter(id=id,user_id=request.user.id).exists():
#         user_like.delete()
#         image = Images.objects.get(id)
#         if image.likes_count==0:
#             image.likes_count=0
#             image.save()
#         else:
#             image.likes_count -=1
#             image.save()

#         return redirect('all-glam/home.html')
    
#     else:
#         likes =Likes.objects.filter(image_id=id,user_id=request.user.id)
#         likes.save_likes()
#         image = Images.objects.get(id)
#         image.likes_count = image.likes_count + 1
#         image.save()
         
#         return redirect('all-glam/home.html')

        
# def comment(request, image_id):
#     image = Images.objects.get(pk=image_id)
#     brief= request.GET.get("comment")
#     print(brief)
#     user = request.user
#     comment = Comments( image = image,brief = brief, user = user)
#     comment.save_comment()

#     return redirect('/')
