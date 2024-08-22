from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    heading = models.CharField(blank=True, max_length=100)
    text = models.TextField(max_length=300)
    photo = models.ImageField(upload_to="photos/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.user.username

