from django.db import models

# Create your models here.
from django.contrib.auth.models import User, auth

# Create your models here.
class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, default="")
    author = models.CharField(max_length=100, default="")
    bookId = models.CharField(max_length=100, default="")
    isbn = models.CharField(max_length=100, default="")
