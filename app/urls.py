from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.post_list, name="post_list"),
    path('posts/', views.post_list, name="post_list"),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/upvote/', views.upvote_post, name="upvote_post"),
    path('<int:post_id>/downvote/', views.downvote_post, name="downvote_post"),
    path('<int:post_id>/comment/', views.add_comment, name="add_comment"),
    
    path('latest/', views.latest_list, name="latest_list"),
    path('tech/', views.tech_list, name="tech_list"),
    path('sports/', views.sport_list, name="sport_list"),
    path('postCreate/', views.post_create, name="post_create"),
    path('<int:post_id>/postEdit/', views.post_edit, name="post_edit"),
    path('<int:post_id>/postDelete/', views.post_delete, name="post_delete"),
    path('register/', views.register, name="register"),
    path('login/', views.user_login, name="login"),
  
]