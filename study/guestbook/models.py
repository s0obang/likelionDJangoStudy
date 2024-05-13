from django.db import models

# Create your models here.
class GuestBook(models.Model):
    name=models.CharField(max_length=30, null=False, blank=False)
    password = models.CharField(max_length=32, null=False, blank=False)
    write_time=models.DateTimeField(auto_now_add=True)
    content=models.TextField()

    def __str__(self):
        return self.name
