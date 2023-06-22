from .views import BlogList, BlogDetail, CreateBlogPost
from django.urls import path

urlpatterns = [
    path('ckeditor/new_post/', CreateBlogPost, name='create'),
    path('', BlogList.as_view(), name='home'),
    path('<slug:slug>/', BlogDetail.as_view(), name='blog_detail'),
]