from django.db import models
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    CATEGORY = (
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
        return f'{self.title}  by  author  {self.author}'


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=50, null=True)
    comment = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    last_edited = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.comment} by user {self.author}'
