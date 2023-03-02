from django.shortcuts import render

from .forms import  User



def registration(request):
    fm = User()
    return render(request,'index.html',{'fm':fm})

