
from django.urls import path
from . import views 

urlpatterns = [
    path("",views.startinPage,name="starting_page"),
    path("posts",views.posts,name="post"),
    path("post/<slug:slug>",views.single_post,name="post-detail")
]
