from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here.

def index(request):
    #return HttpResponse("this is home page")
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")
    #return HttpResponse("this is about page")

def services(request):
    #return HttpResponse("this is services page")
    return render(request, "services.html")

def contact(request):
    #return HttpResponse("this is contact page")

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        
        

        contact = Contact(name = name, email= email, phone=phone, desc = desc, date = datetime.now())
        contact.save()
    return render(request, "contact.html")

