from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    movies = models.ManyToManyField("Movie",blank=True,related_name="who_posted")#find user with alias: who_posted
    def __str__(self) -> str:
        return f"{self.id} {self.username}"
    pass
class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    creator = models.ForeignKey(User,on_delete=models.CASCADE,related_name="creator")
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=8192,default="")
    link = models.URLField(max_length=200)
    def __str__(self):
        return f"{self.id}: {self.creator}, content: {self.content}"
