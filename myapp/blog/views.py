

from django.shortcuts import render,redirect 
from django.http import HttpResponse
from django.urls import reverse
import logging  

# Create your views here.

posts = [{'id': '1', 'title': 'First Post', 'content': 'This is the content of the first post.'},
            {'id': '2', 'title': 'Second Post', 'content': 'This is the content of the second post.'},
            {'id': '3', 'title': 'Third Post', 'content': 'This is the content of the third post.'},
            {'id': '4', 'title': 'Fourth Post', 'content': 'This is the content of the fourth post.'},
    ]    

def index(request):
    blog_title = 'My Awesome Blog'
  
    return render(request,'blog/index.html',{ 'blog_title': blog_title, 'posts': posts })

def details(request,post_id):
   post = next((item for item in posts if item ['id'] ==post_id), None)
#    logger =  logging.getLogger("TESTING")
#    logger.debug(f"Post variable is {post}")
   return render(request, 'blog/details.html', {'post': post})
    # for post in posts:
    #     if post['id'] == str(post_id):
    #         return render(request, 'blog/details.html', {'post': post})

def new_urls(request):
    return HttpResponse('New URLs page')

def old_urls(request):
    return redirect(reverse('blog:new_page_urls'))