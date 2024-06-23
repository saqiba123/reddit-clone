from django.shortcuts import render
from .models import Post
from .forms import PostForm, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm





# Create your views here.
def home(request):
    return render(request,"app/index.html")


# Basic CRUD Operations
#Get list the posts

def post_list(request):
    posts_data = Post.objects.all().order_by('-created_at')
    return render(request, "app/posts_list.html", {"posts":posts_data})
    
#create post
@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            return redirect('post_list')
            
    else:
        form = PostForm()
        
    return render(request, "app/post_form.html", {"form":form})
        
     
 
# edit that post
@login_required
def post_edit(request, post_id):
    post_info = get_object_or_404(Post, pk=post_id, user = request.user)
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES, instance=post_info)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post_info)
    
    return render(request, "app/post_form.html", {"form":form})
     

#delete the post
@login_required
def post_delete(request, post_id):
    post_details = get_object_or_404(Post, pk=post_id, user = request.user)
    if request.method == "POST":
        post_details.delete()
        return redirect('post_list')
    return render(request, "app/post_confirm_delete.html", {"post_detail":post_details})
    
    

# def signIn(request):
#     pass


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            form.save()
            login(request,user)
            return redirect('post_list')
            
    else:
        form = UserRegistrationForm()
    
    return render(request, "registration/register.html",{'form':form})
        



def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('post_list')
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = AuthenticationForm()
    
    return render(request, "registration/login.html", {'form': form})

# def signOut(request):
#     pass

