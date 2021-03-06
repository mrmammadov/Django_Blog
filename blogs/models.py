from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogs-detail', kwargs={'pk': self.id})


class Tag(models.Model):
    choices = [
        ('python', 'python'),
        ('java', 'java'), 
        ('react', 'react')
    ]
    title = models.CharField(max_length=20, choices=choices)
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return self.title