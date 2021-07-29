from django.db import models

# Create your models here.

class Family(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.IntegerField()
    phone_type = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name
