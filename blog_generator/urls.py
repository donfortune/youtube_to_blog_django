from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all-blogs/', views.all_blogs, name='all-blogs'),
    path('blog-details/', views.blog_details, name='blog-details'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_logout, name='log-out'),

]