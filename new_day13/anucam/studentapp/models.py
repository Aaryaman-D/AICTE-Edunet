from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.TextField(max_length=30)
    age=models.IntegerField(default=0)
    email=models.EmailField(max_length=254)
    role=models.CharField(max_length=50, default="student")

    def __str__(self):
        return self.name