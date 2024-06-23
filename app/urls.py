from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('posts/', views.post_list, name="post_list"),
    path('postCreate/', views.post_create, name="post_create"),
    path('<int:post_id>/postEdit/', views.post_edit, name="post_edit"),
    path('<int:post_id>/postDelete/', views.post_delete, name="post_delete"),
    path('register/', views.register, name="register"),
    path('login/', views.user_login, name="login"),
    # path('signOut/', views.signOut, name="signOut"), 
]