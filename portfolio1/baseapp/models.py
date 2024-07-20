from django.db import models
from users.models import CustomUser
# Create your models here.


class Tag(models.Model):


    name = models.CharField(max_length=200)

    def __str__(self) :

        return self.name
        


class Post(models.Model) :

    headline = models.CharField(max_length=200)
    sub_headline = models.CharField(null=True,blank=True,max_length=200)
    body = models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)

    thumbnail = models.ImageField(null=True,blank=True,default="maintemplate_images/defaultpost.webp",upload_to="images")
    #slug = ...

    tags = models.ManyToManyField(Tag)

    def __str__(self) :

        return self.headline
        



class Comment(models.Model) :

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def __str__(self) :

        return f"{self.user.username} , {self.post}"