from django.shortcuts import render,redirect 
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
    return HttpResponse('Hello, World!')

def post_details(request,post_id):
    return HttpResponse(f'Post details page for post {post_id}')

def new_urls(request):
    return HttpResponse('New URLs page')

def old_urls(request):
    return redirect(reverse('blog:new_page_urls'))