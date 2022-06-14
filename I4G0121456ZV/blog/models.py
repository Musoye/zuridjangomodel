from turtle import title
from django.db import models
from django.contrib.auth import get_user_model



# Create your models here.
User = get_user_model()

class Post(models.Model):
    Title = models.CharField(max_length=200) 
    Text = models.TextField(max_length=150)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()
