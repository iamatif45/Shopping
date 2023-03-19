from django.shortcuts import render

from .models import Contact


def index(request):
    return render(request, 'index.html')


def contact1(request):
    thank = False
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, 'contact1.html', {'thank': thank})

def about1(request):
    return render(request,'about1.html')
