from django.shortcuts import render
def check_authenticated(myfunc):  # User Defined Decorator.
    def inner(request):
        if request.user.is_authenticated:
            return render(request,'LMS/home.html')
        else:
            return myfunc(request)
    return inner