from django.db import models

class Post(models.Model):
    write_time=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=60)
    content=models.TextField()

class PostImages(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='post_images/')

# Create your models here.
