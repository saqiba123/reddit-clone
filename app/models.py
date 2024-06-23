from django.db import models
#for user
from django.contrib.auth.models import User
from django.utils import timezone 


# Create your models here.
class Post(models.Model):
    #only user can create post each post have to linked with particular user
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(max_length=240)
    photo = models.ImageField(upload_to="postImages/",blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.user.username} - {self.text[:11]}"
    
    
