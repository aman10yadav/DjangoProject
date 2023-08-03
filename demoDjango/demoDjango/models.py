from django.db import models

class Register(models.Model):
    emailId = models.CharField(max_length=45)
    password = models.CharField(max_length=16)
    mobile = models.CharField(max_length=10)
    fullName = models.CharField(max_length=45)
    address = models.models.CharField(max_length=50)