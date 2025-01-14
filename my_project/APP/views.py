from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import Studentform1
from .models import Student
from .models import Book
from .forms import Bookform

# Create your views here.
def home(request):
    return HttpResponse("welcome")

def index(request):
    f="hello"
    return render(request, 'index.html',{'view':f})

def study(request):
    if request.method=='POST':
        f=Studentform1(request.POST)
        if f.is_valid():
            f.save()
        return HttpResponse("Data is saved")
    
    else:
        x=Studentform1
        return render(request, 'student.html',{'form1':x})
    
    
def studentview(request):
    a=Student.objects.all()
    return render(request, 'studentview.html',{'sview':a})


def datadelete(request,id):
    q=Student.objects.get(id=id)
    q.delete()
    return redirect(studentview)

def editdata(request,id):
    p=Student.objects.get(id=id)
    s=Studentform1(request.POST , instance=p)
    if s.is_valid():
        s.save()
        return redirect(studentview)
    return render(request, 'edit.html',{'edit':p})

def dataupdate(request,id):
    p=Student.objects.get(id=id)
    s=Studentform1(request.POST , instance=p)
    if s.is_valid():
        s.save()
        return redirect(studentview)
    return render(request, 'edit.html',{'edit':p})


def library(request):
    if request.method=='POST':
        f=Bookform(request.POST)
        if f.is_valid():
            f.save()
            return HttpResponse("Data is saved")
    
    else:
        x=Bookform
        return render(request, 'student.html',{'form1':x})