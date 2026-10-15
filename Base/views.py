from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Contact
# Create your views here.


# def home(request):
#     return render(request,'home.html')

def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('number')
        content=request.POST.get('content')
        if len(name)>1 and len(name)<30:
            pass
        else:
            messages.error(request,'size btw 2 and 30')
            return render(request,'home.html')
        if len(email)>1 and len(email)<30:
            pass
        else:
            messages.error(request,'size btw 2 and 30')
            return render(request,'home.html')
        if len(number)>2 and len(number)<11:
            pass
        else:
            messages.error(request,'size btw 2 and 11')
            return render(request,'home.html')

        Contact.objects.create(
            name=name,
            email=email,
            number=number,
            content=content
        )
        
        messages.success(request,'Thanks For Contacting Me')
        return redirect('/')
    return render(request,'home.html')

