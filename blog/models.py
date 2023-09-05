from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    likes = models.ManyToManyField(User, blank=True, null=True, related_name="post_likes")
    post_image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("home")


class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.post.title + " - " + self.user.username


class Profile(models.Model):
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    web_page = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name