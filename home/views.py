from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
# Create your views here.
def index(request):
    context ={
        'variable' :"This is from view"
    }
    return render(request, 'index.html', context)
    # return HttpResponse('This is Homepage')

def about(request):
    return render(request,'about.html')
    # return HttpResponse('This is About page')

def services(request):
    return render(request,'services.html')
    # return HttpResponse('This is Services page')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, desc=desc, date=datetime.today())
        contact.save()
    return render(request,'contact.html')
    # return HttpResponse('This is contact page')
