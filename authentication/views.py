from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from login2.models import faculty,users,committee1,subjects
from login1.forms import RegisterUserForm, committee1Form, facultyForm, subjectsForm,usersForm, userscForm
from django.http import HttpResponseRedirect
# from members.views import register_user
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from login1.forms import RegisterUserForm

# Create your views here.
def home(request):
    return render(request,"authentication/index.html")

def display(request):
    faculty_list=faculty.objects.all()
    return render(request,'authentication/display.html',
    {'faculty_list' : faculty_list})
    
def signup(request):

    # if request.method == 'POST':
    #     Username = request.POST['Username']
    #     FirstName = request.POST['FirstName']
    #     LastName = request.POST['LastName']
    #     Email = request.POST['Email']
    #     Password = request.POST['Password']

    #     myuser = User.objects.create_user(Username,FirstName,LastName,Email,Password)
    #     myuser.FirstName = FirstName
    #     myuser.LastName = LastName

    #     myuser.save()

    #     messages.success(request,'Your Account has been succesfully created.')

    # return redirect('login')

    return render(request,"authentication/signup.html")
        
def login(request):

    # if request.method == 'POST':
    #     Username = request.POST['Username']
    #     Password = request.POST['Password']

    #     user = authenticate(username = Username,password=Password)

    #     if user is not None:
    #         login(request,user)
    #         FirstName = user.FirstName
    #         return render(request,"authentication/login.html",{'FirstName':FirstName})

    #     else:
    #         messages.error(request,"Bad Credentials")
    #         return redirect('home')

    return render(request,"authentication/login.html")

def display(request):
    if request.method== 'post':
        return render(request,'authentication/display.html')
    else:
         return HttpResponse(request,"text files : not found")
    
def landing(request):
    return render(request,"authentication/landing.html")

def subjects3(request):
    return render(request,"authentication/subjects3.html")

def subjects4(request):
    return render(request,"authentication/subjects4.html")

def subjects5(request):
    return render(request,"authentication/subjects5.html")

def subjects6(request):
    return render(request,"authentication/subjects6.html")

def subjects3c(request):
    return render(request,"authentication/subjects3c.html")

def subjects6c(request):
    return render(request,"authentication/subjects6c.html")

def landingc(request):
    return render(request,"authentication/landingc.html")

def loginc(request):
    return render(request,"authentication/loginc.html")

def show_image(request):
    return render(request,"authentication/show_image.html")

def final(request):
    return render(request,"authentication/final.html")

def demo(request):
    return render(request,"authentication/demo.html")    

# def all_display(request):
#     display=faculty.objects.all()
#     return render(request, "authentications/display.html",{'display': display})

def images(request):
    return render(request,"/images")


def add_faculty(request):
    submitted = False
    if request.method=="POST":
        form =facultyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_faculty?submitted=True')
    else:
        form = facultyForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'authentication/add_faculty.html',{'form': form,'submitted':submitted})

def add_users(request):
    submitted = False
    if request.method=="POST":
        form =usersForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_users?submitted=True')
    else:
        form = usersForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'authentication/add_users.html',{'form': form,'submitted':submitted})

def add_usersc(request):
    submitted = False
    if request.method=="POST":
        form =usersForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_usersc?submitted=True')
    else:
        form = userscForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'authentication/add_usersc.html',{'form': form,'submitted':submitted})

def add_committee(request):
    submitted = False
    if request.method=="POST":
        form =committee1Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_committee?submitted=True')
    else:
        form = committee1Form
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'authentication/add_committee.html',{'form': form,'submitted':submitted})

def sub_image(request):
    submitted = False
    if request.method=="POST":
        form =subjectsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/sub_image?submitted=True')
    else:
        form = subjectsForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'authentication/sub_image.html',{'form': form,'submitted':submitted})

# def show_image(request):
#     submitted = False
#     if request.method=="GET":
#         form =subjectsForm(request.GET,request.FILES)
#         return HttpResponseRedirect('/show_image?submitted=True')
#     else:
#         form = subjectsForm
#         if 'submitted' in request.POST:
#             submitted=True
#     return render(request,'authentication/show_image.html',{'form': form,'submitted':submitted})

def register_user(request):
    if request.method=="POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data['username']
            # firstname = form.cleaned_data['firstname']
            # lastname = form.cleaned_data['lastname']
            # email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            # password = form.changed_data['password2']
            user = authenticate(username=username,password=password)
            # login(request,user)
            messages.success(request,("registered successfully...!!"))
            return redirect('/add_users')
    else:
        form = RegisterUserForm()

    return render(request,'authentication/register_user.html',{'form': form})

def login_user(request):
    if request.method == "POST":
        username=request.post['username']
        password=request.post['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
           return redirect('login')

    else:
        return render(request,'authentication/adlogin.html',{})
    






