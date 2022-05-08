from django.db import models

# Create your models here.
class details_of_incident(models.Model):
    Name=models.CharField(max_length=100)
    PhoneNumber=models.BigIntegerField()
    email=models.EmailField(max_length=254)
    incident=models.CharField(max_length=1000)
    Address=models.CharField(max_length=500, default="null")
    comments=models.TextField(max_length=1000, default="null")
    file=models.ImageField(null=True,blank=True)

    