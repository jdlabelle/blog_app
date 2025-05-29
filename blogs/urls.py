"""Defines URL patterns for blogs"""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
        # Home Page
        path('', views.index, name='index'),
        # Individual Blog Posts
        path('post/<int:post_id>/', views.post, name='post'),
        # Page for adding a new blog category
        path('new_blog/', views.new_blog, name='new_blog'),
        # Page for adding a new post
        path('new_post/', views.new_post, name='new_post'),
        # Page for editing a post
        path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
        ]
