from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=30)
    department = models.CharField(max_length=35)
    desgination = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField()
    dateofjoin = models.DateField()

    def __str__(self):
        return str(self.id) +" "+ self.name