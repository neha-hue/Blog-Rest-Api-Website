from django.contrib import admin
from home.models import Contact
from home.models import Post
from home.models import Comment,Profile

# Register your models here.
admin.site.register(Contact)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Profile)
