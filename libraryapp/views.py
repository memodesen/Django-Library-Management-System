from django.http.response import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
import datetime
from .models import Users
from .models import Books
from .forms import AppLoginForm
from .forms import AppRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import redirect


def index(request):
    return render (request,"index.html")

def admin_login(request):
    return redirect('admin:index')

def register(request):

     if request.method=='POST':
           form=AppRegisterForm(request.POST)

           if form.is_valid():
                 p=Users(name=form.cleaned_data["name"],surname=form.cleaned_data["surname"],email=form.cleaned_data["email"],password=form.cleaned_data["password"],username=form.cleaned_data["username"]   )
                 p.save()
                 return HttpResponseRedirect("index")

     else:
       form=AppRegisterForm()
     
     return render (request,"register.html",{
          "form":form
    }    )   
                   
   
def loginn(request):
    if request.method == 'POST':
        form = AppLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print(user)
                return redirect('books')
            else:
                #There is a problem in authentication function that i couldnt find the solution in google or anywhere. I will fix it soon.
                print(user)
                return redirect('books')
                
    else:
        form = AppLoginForm()
    return render(request, 'loginn.html', {'form': form})
           


def user(request):
    return render (request,"user.html")


def issue(request):
    users = Users.objects.all()
    return render(request, 'issue.html', {'users': users})

def books(request):
    books=Books.objects.all()
    return render (request,"books.html",{'books':books})

def logout_view(request):   
    logout(request)
    return redirect('index')

