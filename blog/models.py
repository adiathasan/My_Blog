from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Post(models.Model):
    CATEGORY = (
        ('Lifestyle', 'Lifestyle'),
        ('Health', 'Health'),
        ('Family', 'Family'),
        ('Lifestyle', 'Lifestyle'),
        ('Health', 'Health'),
        ('Family', 'Family'),
        ('Management', 'Management'),
        ('Travel', 'Travel'),
        ('Work', 'Work'),
    )
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    pub_date = models.DateTimeField(blank=True, null=True)
    last_edited = models.DateTimeField(null=True, blank=True)
    category = models.CharField(null=True, max_length=50, choices=CATEGORY)

    image = models.ImageField(blank=True, null=True)

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return f'{self.title}  by author  {self.author}'


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=50, null=True)
    comment = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(default=timezone.now)
    last_edited = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.comment} by user {self.author}'


class User_Account(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(null=True, max_length=100)
    phone = models.IntegerField(null=True, editable=True)
    profile_pic = models.ImageField(blank=True, null=True)

    def __str__(self):
        return str(self.author)

# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#    if created:
#       User_Account.objects.create(author=instance)


# post_save.connect(create_profile, sender=User)


# @receiver(post_save, sender=User)
# def update_profile(sender, instance, created, **kwargs):
# if not created:
# instance.User_Account.save()

# post_save.connect(update_profile, sender=User)
