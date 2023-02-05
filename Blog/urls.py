from django.urls import path
from .views import blog_list, blog_detail, blog_tag

app_name = 'Blog'

urlpatterns = [
    path('', blog_list, name='blog_list'), # blog/list
    path('detail/<int:blog_id>/', blog_detail, name='blog_detail'),  # blog/detail
    path('tag/<str:tag_title>/', blog_tag, name='blog_tag'),  # blog/detail
]