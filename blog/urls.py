from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home_blog, name='home'),
    path('category/', views.category, name='category'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/<int:pk>/', views.perticular_blog, name='blog'),
    path('edit_page/', views.edit_post, name='edit'),
]


