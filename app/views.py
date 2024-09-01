from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render
from .models import Post , Comment
from .forms import PostForm, UserRegistrationForm , CommentForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required 
from django.views.decorators.http import require_POST
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.utils import timezone


# Create your views here.
# def home(request):
#     return render(request,"app/index.html")

#===============================================SPORTS PAGE ===========================================================
def sport_list(request):
    posts_data = Post.objects.filter(text__icontains="sport").order_by('-created_at')
    comment_form = CommentForm()
    return render(request, "app/posts_list.html", {"posts":posts_data, 'comment_form': comment_form})


#==============================================TECH PAGE =============================================================
def tech_list(request):
    posts_data = Post.objects.filter(text__icontains="tech").order_by('-created_at')
    comment_form = CommentForm()
    return render(request, "app/posts_list.html", {"posts":posts_data, 'comment_form': comment_form})


#==============================================LATEST PAGE =========================================================
def latest_list(request):
    today = timezone.now().date()
    posts_data = Post.objects.filter(created_at__date=today).order_by('-created_at')
    comment_form = CommentForm()
    return render(request, "app/posts_list.html", {"posts":posts_data, 'comment_form': comment_form})



#===================================== UPVOTE + DOWNVOTE + COMMENTS =========================================================================
# @login_required
@require_POST
def upvote_post(request, post_id):
    if not request.user.is_authenticated:
        messages.success(request, "You are not logged in!")
        return redirect('post_list')  # Redirect to the posts page
    
    post = get_object_or_404(Post, id=post_id)
    post.upvotes += 1
    post.save()
    return JsonResponse({'upvotes': post.upvotes})

# @login_required
@require_POST
def downvote_post(request, post_id):
    if not request.user.is_authenticated:
        messages.success(request, "You are not logged in!")
        return redirect('post_list')  # Redirect to the posts page
    
    post = get_object_or_404(Post, id=post_id)
    post.downvotes += 1
    post.save()
    return JsonResponse({'downvotes': post.downvotes})


# @require_POST
# @login_required

def add_comment(request, post_id):
    if not request.user.is_authenticated:
        messages.success(request, "You are not logged in!")
        return redirect('post_list')  # Redirect to the posts page
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('post_detail', post_id=post.id)  # Redirect to the post's detail page
    
    return redirect('post_detail', post_id=post.id)  



#=========================================== Basic CRUD Operations =============================================
#Get list the posts
def post_list(request):
    posts_data = Post.objects.all().order_by('-created_at')
    comment_form = CommentForm()
    return render(request, "app/posts_list.html", {"posts":posts_data, 'comment_form': comment_form})


# @login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()  # Get all comments related to the post
    return render(request, 'app/post_detail.html', {'post': post, 'comments': comments})

    
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
    

#=====================================================AUTHENTICATION =================================================================

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
        initial_data = {'username':"",'password1':"",'password2':"",'email':""}
        form = UserRegistrationForm(initial=initial_data)
    
    return render(request, "registration/register.html",{'form':form, 'show_search_bar': False})
        



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










