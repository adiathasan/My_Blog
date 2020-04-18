from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.Home_blog, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/<int:pk>/', views.particular_blog, name='blog'),
    path('create_page/', views.create_post, name='edit'),
    path('update_page/<int:pk>/', views.update_post, name='update'),
    path('draft_page/', views.draft_post, name='draft'),
    path('post/<int:pk>/', views.post_blog, name='post'),
    path('login/', views.login, name='login'),
    path('logout/', views.logoutpage, name='logout'),
    path('register/', views.register, name='register'),
    path('comment/<int:pk>/', views.comment_post, name='comment'),
    path('comment/<int:pk>/remove/', views.remove_comment, name='remove'),
    path('delete/<int:pk>/', views.delete_post, name='delete'),
    path('comment/<int:pk>/remove/', views.remove_comment, name='remove'),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name='blog/reset_password.html'),
         name='reset_password'),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='blog/email_message.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='blog/new_password.html'),
         name='password_reset_confirm'),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='blog/messege_sent.html'),
         name='password_reset_complete'),

]
