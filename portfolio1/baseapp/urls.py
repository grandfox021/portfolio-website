from django.urls import path
from . import views


urlpatterns = [

path("" ,views.homepage, name='home' ),
path("blog/" ,views.get_posts, name='blog' ),
path("blog/<str:pk>" ,views.get_post_id, name='post' ),


]