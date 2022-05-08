from email.headerregistry import Address
from email.mime import image
from http.client import HTTPResponse
import re
from django.shortcuts import render
from django.http import HttpResponse

from .models import details_of_incident
# Create your views here.
def index(request):
    return render(request,'index.html')

def form(request):
     print("submitted")
     if request.method=="POST":
        Name=request.POST.get("Name")
        PhoneNumber=request.POST.get("PhoneNumber")
        email=request.POST.get("email")
        Address=request.POST.get("Address")
        incident=request.POST.get("incident")
        comments=request.POST.get("comments")
        file=request.FILES['file']
        print(request.FILES.get('file'))
        print(Name)
        print(PhoneNumber)
        print(email)
        print(Address)
        print(incident)
        print(comments)
        create=details_of_incident(Name=Name,PhoneNumber=PhoneNumber,email=email,Address=Address,incident=incident,comments=comments,file=file)
        create.save()
        
        img = details_of_incident.objects.all()
     img = details_of_incident.objects.all()
     print("============ data base")
     print(img)

     return render(request,'data.html' , context={"img" : img})

# def getimg(request):
#     img = details_of_incident.objects.all()
#     print("============ data base")
#     print(img)
#     return render(request,'index.html',context={"img" : img})
