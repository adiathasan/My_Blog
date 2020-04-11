from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.Home_blog, name='home'),
    path('category/', views.category, name='category'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/<int:pk>/', views.perticular_blog, name='blog'),
    path('create_page/', views.create_post, name='edit'),
    path('update_page/<int:pk>/', views.update_post, name='update'),
    path('draft_page/', views.draft_post, name='draft'),
    path('post/<int:pk>/', views.post_blog, name='post'),
    path('login/', views.login, name='login'),
    path('logout/', views.logoutpage, name='logout'),
    path('register/', views.register, name='register'),

]


