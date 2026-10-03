from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path("details/<int:post_id>", views.details, name='post_details'),
    path("new_urfsdfdffffd fdsfsdls/", views.new_urls, name='new_page_urls'),
    path('old_urls/',views.old_urls, name='old_urls'),
]