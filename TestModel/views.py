from django.shortcuts import render
from django.http import HttpResponse
from TestModel.models import Goals, Account
from django.contrib import auth
from django.shortcuts import render, redirect
import json
from django.http import JsonResponse


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

def store_goals(data):
    cnt = len(Goals.objects.all())
    goalTitle = data.get("goalTitle")
    subgoals = data.get("subgoals")
    timelineDate = data.get("timelineDate")
    timelineTime = data.get("timelineTime")
    goals = Goals(cnt, goalTitle, subgoals, timelineDate, timelineTime)
    goals.save()

def scan_goals():
    goals = Goals.objects.all()
    goals_dic = {}
    for g in goals:
        goals_dic[g.id] = [g.goalTitle,g.subgoals,g.timelineDate,g.timelineTime]
    return goals_dic
def goals(request):
    if request.method == 'GET':
        goals = scan_goals()
        print(goals)
        return render(request,"goals.html", {"goals":goals})
def dashboard(request):
    if request.method == 'GET':
        return render(request, 'dashboard.html')
    if request.method == 'POST':
        print("post is detected")
        data = json.loads(request.body)
        store_goals(data)
        goals = scan_goals
        return JsonResponse({'message': str(goals)}, status=200)

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