from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Suscribe(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.email

class ContactUs(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)
    message= models.TextField()

    def __str__(self):
        return self.name

class Addpost(models.Model):
    username = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    img = models.ImageField("Image", null=True)
    title = models.TextField("Title", max_length=200, null=True)
    published = models.DateTimeField("Date Published", auto_now_add=True, null=True)
    