from django.db import models
from django.contrib.auth.models import User


class login(models.Model):
    ename=models.CharField(max_length=20)
    eage=models.IntegerField()
    eno=models.CharField(max_length=15)
    eaddress=models.CharField(max_length=50)
    epassword = models.CharField(max_length=10)
    user=models.ForeignKey(User,on_delete=models.CASCADE)







from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http.response import HttpResponse
from .forms import MyUserform

def view_register(request):
    if request.method=="GET":
        userform=UserCreationForm()
        myUserform=MyUserform()
        d1={'form':userform,'myuser':myUserform}
        return render(request,'Users/registration.html',context=d1)
    elif request.method=="POST":
        userform=UserCreationForm(request.POST)
        myUserform=MyUserform(request.POST)
        if(userform.is_valid and myUserform.is_valid()):
            u=userform.save()
            mu=myUserform.save()
            mu.user=u
            mu.save()
            return HttpResponse("User register successfully")
        else:
            return render(request,'Users/registration.html',context=d1)