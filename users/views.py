from django.shortcuts import render,redirect
from .forms import StudentRegisterForm,MyAuthenticationForm,StudentUpdateForm
from django.contrib.auth import authenticate,logout,login
from contributions.models import Contribution
from .models import Student
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def student_register(request):
    if request.method == 'GET':
        form = StudentRegisterForm()
        context = {
            'form' : form,
            'title' : 'Student Register'
        }
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST,request.FILES)
        context = { 'form' : form }
        if form.is_valid():    
            form.save()
            return redirect('home')
    return render(request, 'student_register.html',context)

@login_required
def contact_user(request,pk):
    author = Student.objects.get(id=pk)
    context = {
        'author' : author,
        'title' : 'Contact Author'
    }
    return render(request,'contact_user.html',context)

@login_required
def profile(request):
    profile_owner = Student.objects.get(id=request.user.id)
    context = { 'profile' : profile_owner, 'title' : 'Profile' }
    return render(request,'user_profile.html',context)


@login_required
def edit_profile(request):
    student = Student.objects.get(id=request.user.id)
    if request.method == 'GET':
        form = StudentUpdateForm(instance=student)
    else:
        form = StudentUpdateForm(request.POST,request.FILES,instance=student)
        if form.is_valid():
            form.save()
            messages.success(request,"Profile updated successfully 🥳.")
            return redirect('profile')
    context = { 'form' : form }
    return render(request,'edit_profile.html',context)


