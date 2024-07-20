from django.shortcuts import render,HttpResponse
from users.models import CustomUser
from .models import Post,Tag,Comment

# Create your views here.


def homepage(request) :

    return render(request,'home.html')


def profilepage(request) :

    return render(request,'base/portfolio-details.html')

def get_posts(request) :

    posts = Post.objects.all()

    context ={

        'posts' : posts
    }

    return render(request,'blog.html',context)

def get_post_id(request,pk) :

    post = Post.objects.get(id=pk)

    context = {'post' : post}


    # create comment  ... #

    if request.method == "POST" and "submit" in request.POST :

        if request.user is None :

            name = request.POST.get("commenter_name")

        else :

            name = CustomUser.objects.get(username = request.user.username)

        content = request.POST.get("text_body")
        user = name
        


    return render(request ,'postpage.html',context)

    


def login(reuquest) :

    pass


def logout(request) :

    pass



# def create_commnet(request) :

#     if request.method == "POST" :

#         if request.user is None :

#             name = request.POST.get("commenter_name")

#         else :

#             name = CustomUser.objects.get(username = request.user.username)

#         content = request.POST.get("text_body")
#         user = name



#     pass