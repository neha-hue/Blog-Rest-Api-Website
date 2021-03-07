from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField
import datetime
import time

# Create your models here.
#makemigrations-create changes and store in a file
#migrate-apply ther pending changes created by makemigrations
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=122)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name

class Profile(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio=models.TextField()
    profile_pic=models.ImageField(null=True,blank=True,upload_to="images/profile/")
    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        #return reverse('post_detail',args=(str(self.id)))
        return reverse('post_list')




class Post(models.Model):
    title=models.CharField(max_length=255)
    header_image=models.ImageField(null=True,blank=True,upload_to="images/")
    title_tag=models.CharField(max_length=255)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    #body=models.TextField()
    body=RichTextField(blank=True,null=True)

    post_date_field=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + '|'+str(self.author)

    def get_absolute_url(self):
        #return reverse('post_detail',args=(str(self.id)))
        return reverse('post_list')

class Comment(models.Model):
    post=models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    body=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s -%s' % (self.post.title,self.name)


    


    

   