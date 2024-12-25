# web/views.py
from django.http import HttpResponse
from django.shortcuts import render,redirect
from web.forms import Employee, EmployeeForm
from web.models import WangUser
# from web.forms import UserReg
from web import models

def index(request):
    return render(request, 'index.html')

def home(request):
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/about')
            except:
                pass
    else:
        form =EmployeeForm()
    return render(request,'home.html',{'Details':form})        


def about(request):
    employees=Employee.objects.all()
    return render(request,"about.html",{'badal':employees})
def delete(request,id):
    emp=Employee.objects.get(id=id)
    emp.delete()
    return redirect('/about')
def edit(request,id):
    emp=Employee.objects.get(id=id)
    return render(request,"edit.html",{'employee':emp})
def update(request,id):
    employee=Employee.objects.get(id=id)
    form =EmployeeForm(request.POST,instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/about")
    return render(request,'edit.html',{'employee':employee})

def contact(request):
    return render(request, 'contact.html')

def filter(request):
    return render(request,'filter.html')

def search(request):
    if request.method=="POST":
        id=request.POST.get('ID')
    employees=Employee.objects.filter(id=id)
    return render(request,"show.html",{'badal':employees})

def show(request):
    employees=Employee.objects.all()
    return render(request,"show.html",{'badal':employees})

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        user_list=models.WangUser.objects.filter(username=username)
        error_name=[]

        if user_list:
            error_name='This user name already exists'
            return render(request,'register.html',{'error_name':error_name})
        else:
            username=models.WangUser.objects.create(username=username,password=password,email=email)
            username.save()
        return redirect('login')
    return render(request,'register.html')
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        obj_user=models.WangUser.objects.filter(username=username,password=password)
        if obj_user:
            return redirect('/home')
        error='Wrong username and password'
    return render(request,'login.html',locals())
    
def landing(request):
    return render(request,'landing.html')
def setcookies(request):
    res=render(request,'setcookie.html')
    res.set_cookie('name','badal')
    res.set_cookie('password','12345')

    res.set_cookie('name','badal',max_age=60)
    res.set_cookie('password','12345',max_age=60)
    return res


def getcookies(request):
    name=request.COOKIES['name']
    password=request.COOKIES['password']

    return render(request,'getcookie.html',{'name2':name,'pass':password})


def deletecookie(request):
    res=render(request,'deletecookie.html')
    res.delete_cookie('name')
    res.delete_cookie('pass')
    return res