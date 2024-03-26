from django.shortcuts import render

from django.http import HttpResponse

from TestModel.models import Goals, Account
from django.contrib import auth
from django.shortcuts import render, redirect

def testdb(request):
    goals = Goals(create_date='2024.3.10', content='finish proposal')
    goals.save()
    return HttpResponse("<p>a new goal finish proposal is added successfully</p>")

def login(request):
    if request.method == 'POST':
        print('post login')
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = Account.objects.filter(email = email)
        for u in user:
            if u.password == password:
                print('login successfully')
                # return HttpResponse("<p>login succeess</p>")
                return redirect("/TestModel/dashboard/")
        print('login fail')
        return HttpResponse("<p>login fail</p>")
    if request.method == 'GET':
        print('login page')
        return render(request, 'login.html')

def dashboard(request):
    if request.method == 'GET':
        return render(request, 'dashboard.html')

from django.contrib.auth.models import User
def register(request):
    if request.method == 'POST':
        print("post register")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        new_account = Account(username= username,email = email, password= password)
        new_account.save()
        print('register successfully')
        return HttpResponse("<p>register successfully</p>")
    if request.method == 'GET':
        print("register page !")
        return render(request, 'register.html')

def homepage(request):
    if request.method == 'GET':
        return render(request, 'homepage.html')