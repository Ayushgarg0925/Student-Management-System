from django.shortcuts import redirect, render
from django.http import HttpResponse
from SMS_APP.models import *
from SMS_APP.decorator import *
from django.contrib.auth import *

# def home(request):
#     if request.method=='GET':
#         return render(request,'SMS_APP/index.html')          
#     elif request.method=='POST':
#         try:
#             username=request.POST.get('i1','NA')
#             userpwd=request.POST.get('p1','NA')
#             if username=='admin' and userpwd=='admin':
#                 data=login.objects.all()
#                 d1={'c':data}
#                 return render(request,'SMS_APP/show_all.html', context=d1) 
#             else:
#                 a=login.objects.get(ename=username,epassword=userpwd)
#                 d1={
#                     'a':username,
#                     'c':a,
#                 }
#                 return render(request,'SMS_APP/show.html', context=d1)    
#         except:
#             return HttpResponse('<h1>wrong Id or Password</h1><br><a href="http://127.0.0.1:8000">Back</a>')
        
@check_authenticated
def home(request):
    if request.method=='GET':
        resp=render(request,'SMS_APP/index.html')
        return resp
    elif request.method=='POST':
        username=request.POST.get('i1','NA')
        userpwd=request.POST.get('p1','NA')
        user=authenticate(username=username,password=userpwd)
        if user is not None:
            login(request,user)
            a=login.objects.get(ename=username,epassword=userpwd)
            d1={
                    'a':username,
                    'c':a,
                }
            return render(request,'SMS_APP/show.html', context=d1) 
        else:
            resp=render(request,'SMS_APP/index.html')
            #resp=HttpResponse("<h1>Login Failed!!</h1>")
            return resp
            
def log_in(request):
    if request.method=='GET':
        return render(request,'SMS_APP/login.html')          
    elif request.method=='POST':
        username=request.POST.get('i1','NA')
        userage=int(request.POST.get('i2',0))
        userno=request.POST.get('i3',0)
        useraddress=request.POST.get('i4','NA')
        userpwd=request.POST.get('i5','NA')
        i=login()
        i.ename=username
        i.eage=userage
        i.eno=userno
        i.eaddress=useraddress
        i.epassword=userpwd
        i.save()
        # return HttpResponse('<script>alert("Hello! I am an alert box!!");</script>')       
        return HttpResponse('<h1>data add successfully!!!</h1><a href="/">Back</a>')       
    




    
     
def edit_page(request,a):
    if request.method == 'GET':
        return render(request,'SMS_APP/edit.html')
    elif request.method == 'POST':
        if login.objects.filter(id=a).exists():
            username=request.POST.get('i1','NA')
            userage=int(request.POST.get('i2',0))
            userno=request.POST.get('i3',0)
            useraddress=request.POST.get('i4','NA')
            userpwd=request.POST.get('i5','NA')
            login.objects.filter(id=a).update(ename=username,eage=userage,eno=userno,eaddress=useraddress,epassword=userpwd)
            return render(request,'SMS_APP/show.html')

def delete_data(request,a):
    login.objects.filter(id=a).delete()
    return HttpResponse('<h1>data delete successfully!!!</h1><a href="http://127.0.0.1:8000">Back</a>')


def showall_edit_page(request,a):
    if request.method == 'GET':
        sm=login.objects.get(id=a)
        d1={'sm':sm}
        return render(request,'SMS_APP/edit.html',context=d1)
    elif request.method == 'POST':
        if login.objects.filter(id=a).exists():
            username=request.POST.get('i1','NA')
            userage=int(request.POST.get('i2',0))
            userno=request.POST.get('i3',0)
            useraddress=request.POST.get('i4','NA')
            userpwd=request.POST.get('i5','NA')
            login.objects.filter(id=a).update(ename=username,eage=userage,eno=userno,eaddress=useraddress,epassword=userpwd)
            # return render(request,'SMS_APP/index.html')
            return redirect('http://127.0.0.1:8000')



def delete_data_allpage(request,a):
    login.objects.filter(id=a).delete()
    # return render(request,'SMS_APP/show_all.html')
    return redirect('/registration/')