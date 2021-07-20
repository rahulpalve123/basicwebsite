from django import http
from django.shortcuts import render,HttpResponse
from datetime import date, datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        'varibale':'45'
    }
    return render(request,'index.html',context)
    #return HttpResponse("This is homepage")

def about(request):
    return render(request,'about.html')
    #return HttpResponse("Thid id abot page")

def services(request):
    return render(request,'services.html')
    #return HttpResponse("Thids is services page")

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request,'You details are saved')

    return render(request,'contact.html')
    #return HttpResponse("This is Services page")

