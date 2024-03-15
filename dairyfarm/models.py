from django.db import models

class Users(models.Model):
    username=models.CharField(max_length=50,default='')
    email=models.EmailField(primary_key=True,unique=True)
    password=models.CharField(max_length=50)


    class Meta:
        db_table='Users'

class Buy(models.Model):
    quantity=models.IntegerField()
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=10)
    name=models.CharField(max_length=50)
    type=models.CharField(max_length=50,default='')

    class Meta:
        db_table='Buy'