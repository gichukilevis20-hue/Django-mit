from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    course = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name } - {self.course}"
        