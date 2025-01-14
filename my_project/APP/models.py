from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    
    def __str__(self):
        return self.name
    
# Library models

class Book(models.Model):
    bookname=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    discrption=models.TextField(max_length=200)
    
    def __str__(self):
        return self.bookname