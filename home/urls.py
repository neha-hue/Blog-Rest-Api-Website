from django.contrib import admin
from django.urls import path
from home import views
from .views import PostView
from .views import PostDetailView
from .views import PostUpdateView,PostDeleteView,PostAddView,RegisterUserView,PostCommentView


urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("makeup",views.makeup,name='makeup'),
    path("contact",views.contact,name='contact'),
    path("doctor",views.doctor,name='doctor'),
    path("wedding",views.wedding,name='wedding'),
    path("fashion",views.fashion,name='fashion'),
    path("painter",views.painter,name='painter'),
    path("jwellery",views.jwellery,name='jwellery'),
    path("food",views.food,name='food'),
    path("recipe",views.recipe,name='recipe'),
    path("clothes",views.clothes,name='clothes'),
    path("travel",views.travel,name='travel'),
    path("post-list",PostView.as_view(),name="post_list"),
    path("post_detail/<int:pk>",PostDetailView.as_view(),name="post_detail"),
    path("post_detail/editpost/<int:pk>",PostUpdateView.as_view(),name='editpost'),
    path("post_detail/<int:pk>/remove",PostDeleteView.as_view(),name='delete_post'),
    path("post_add/",PostAddView.as_view(),name='post_add'),
    path("register/",RegisterUserView.as_view(),name='register'),
    path("post_detail/<int:pk>/comments/",PostCommentView.as_view(),name='comments'),


    
]
