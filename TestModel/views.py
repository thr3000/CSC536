from django.shortcuts import render
from django.http import HttpResponse
from TestModel.models import Goals, Account
from django.contrib import auth
from django.shortcuts import render, redirect
import json
from django.http import JsonResponse

def testdb(request):
    goals = Goals(create_date='2024.3.10', content='finish proposal')
    goals.save()
    return HttpResponse("<p>a new goal finish proposal is added successfully</p>")

def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get("email")
        password = data.get("password")
        user = Account.objects.filter(email = email)
        for u in user:
            if u.password == password:
                return JsonResponse({'message': 'login successfully'}, status=200)
        return JsonResponse({'message': 'login failed'}, status=500)
    if request.method == 'GET':
        return render(request, 'login.html')

def dashboard(request):
    if request.method == 'GET':
        return render(request, 'dashboard.html')

from django.contrib.auth.models import User
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        new_account = Account(username=username, email=email, password=password)
        new_account.save()
        return JsonResponse({'message': 'register successfully'}, status=200)
    elif request.method == 'GET':
        return render(request, 'register.html')

def homepage(request):
    if request.method == 'GET':
        return render(request, 'homepage.html')