from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from . models import User
from . forms import StudentRegistration
from django.http.response import HttpResponse



def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()
            Stud = User.objects.all()
            return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': Stud})
        

    else:
        fm = StudentRegistration()
        Stud = User.objects.all()
        return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': Stud})




def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            Stud = User.objects.all()
            return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': Stud})
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
        return render(request, 'enroll/updatestudent.html', {'form': fm})




def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        fm = StudentRegistration()
        Stud = User.objects.all()
        return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': Stud})
