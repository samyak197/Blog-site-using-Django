from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    blog_title = models.CharField(max_length=50)
    blog_content = models.TextField()
    pb_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, max_length=50, on_delete=models.CASCADE)
    category = models.CharField(max_length=40)
    tag = models.CharField(max_length=40)

    def __str__(self):
        return self.blog_title
