from django.urls import path
from blog.api.views import api_details_blog_view, api_update_blog_view, api_delete_blog_view, api_create_blog_view

app_name = 'Blog'

urlpatterns = [
    path('<id>', api_details_blog_view, name='details'),
    path('create/', api_create_blog_view, name='create'),
    path('update/<id>', api_update_blog_view, name='update'),
    path('delete/<id>', api_delete_blog_view, name='delete'),
]
