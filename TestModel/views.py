from django.shortcuts import render
from django.http import HttpResponse
from TestModel.models import Goal, Account, Subgoal
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
    goal = Goal(
        goalTitle=data.get("goalTitle"),
        timelineDate=data.get("timelineDate"),
        timelineTime=data.get("timelineTime")
    )
    goal.save()

    for subgoal_data in data.get("subgoals", []):
        print(subgoal_data)
        subgoal = Subgoal(
            goal=goal,
            title=subgoal_data.get("title"),
            timelineDate=subgoal_data.get("timelineDate"),
            timelineTime=subgoal_data.get("timelineTime")
        )
        subgoal.save()

def scan_goals():
    goals_dic = {}
    for goal in Goal.objects.prefetch_related('subgoal_set').all():
        goals_dic[goal.id] = {
            'goalTitle': goal.title,
            'timelineDate': goal.timelineDate,
            'timelineTime': goal.timelineTime,
            'subgoals': [
                {
                    'title': subgoal.title,
                    'timelineDate': subgoal.timelineDate,
                    'timelineTime': subgoal.timelineTime
                } for subgoal in goal.subgoal_set.all()
            ]
        }
    return goals_dic

def dashboard(request):
    if request.method == 'GET':
        return render(request, 'dashboard.html')
    elif request.method == 'POST':
        data = json.loads(request.body)
        store_goals(data)
        goals = scan_goals()
        return JsonResponse({'goals': goals}, status=200)

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