from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all-blogs/', views.all_blogs, name='all-blogs'),
    path('blog-details/', views.blog_details, name='blog-details'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),

]