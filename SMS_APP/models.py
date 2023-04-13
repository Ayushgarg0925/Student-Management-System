from django.db import models


class login(models.Model):
    ename=models.CharField(max_length=20)
    eage=models.IntegerField()
    eno=models.CharField(max_length=15)
    eaddress=models.CharField(max_length=50)
    epassword = models.CharField(max_length=10)