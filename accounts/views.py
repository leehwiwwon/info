from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Member


def signup(request):
    if request.method == 'POST':
        if request.POST.get('password1') == request.POST.get('password2'):
            email = request.POST.get('email')
            name = request.POST.get('name')
            password = request.POST.get('password1')
            member = Member(email=email, name=name, password=password)
            member.save()
            return HttpResponseRedirect('/')
        return render(request, 'signin.html')
    return render(request, 'signup.html')


def login(request):
    target_url = reverse('roadmap:api')
    if request.method == 'POST':
        member = Member.objects.filter(email=request.POST['email']).first()
        if member is None:
            return render(request, 'login.html', {'error': 'Email is incorrect'})
        if member.password == request.POST['password1']:
            return redirect(target_url)
        return render(request, 'login.html')
    return render(request, 'login.html')


def signin(request):
    render(request,'signin.html', {})


def logingin(request):
    render(request, 'api.html')