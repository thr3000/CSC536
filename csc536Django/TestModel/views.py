from django.shortcuts import render

from django.http import HttpResponse

from TestModel.models import Goals, Account
from django.contrib import auth
from django.shortcuts import render

def testdb(request):
    goals = Goals(create_date='2024.3.10', content='finish proposal')
    goals.save()
    return HttpResponse("<p>a new goal finish proposal is added successfully</p>")


from django.contrib.auth.models import User
def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        new_account = Account(username= username,password= password)
        new_account.save()
        print('login successfully')
        return HttpResponse("login successfully")
    if request.method == 'GET':
        return render(request, 'login.html')