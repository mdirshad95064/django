from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    views = {}
    views['reviews'] = Review.objects.all()

    return render(request,'index.html',views)

def about(request):
    
    return render(request,'about.html')

def services(request):
    views = {}
    views['service'] = Services.objects.all()
    
    return render(request,'services.html')

def portfolio(request):

    return render(request,'portfolio.html')

def price(request):

    return render(request,'price.html')

def blog(request):

    return render(request,'blog-home.html')

def blog(request):

    return render(request, 'blog-single.html')

def pages(request):

    return render(request,'elements.html')

def contact(request):
    views = {}
    views['infos'] = Information.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        data = Contact.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message
        )
        data.save()

    return render(request,'contact.html')