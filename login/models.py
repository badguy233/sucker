from django.db import models

# Create your models here.
class Login(models.Model):
    lname = models.CharField(max_length=20)
    lpassword = models.CharField(max_length=20)
    lemail = models.CharField(max_length=50)


