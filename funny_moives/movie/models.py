from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    def __str__(self) -> str:
        return f"{self.id} {self.username}"
    pass
class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    creator = models.ForeignKey(User,on_delete=models.CASCADE,related_name="creator")
    timestamp = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=200,blank=False)
    def __str__(self):
        return f"{self.id}: {self.creator}, link: {self.link}"

class MovieView(models.Model):
    title = models.CharField(max_length=200,blank=False)
    creator_mail = models.CharField(max_length=200,blank=False)
    description = models.CharField(max_length=200,blank=False)
    link = models.CharField(max_length=200,blank=False)
    def __str__(self):
        return f"title: {self.title}, link: {self.link},des: {self.description}"