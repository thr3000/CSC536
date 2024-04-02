from django.shortcuts import render
from django.http import HttpResponse
from TestModel.models import Goal, Account, Subgoal
from django.contrib import auth
from django.core.serializers.json import DjangoJSONEncoder
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
                return JsonResponse({'message': 'login successfully', 'username': u.username, 'userid': u.id}, status=200)
        return JsonResponse({'message': 'login failed'}, status=500)
    if request.method == 'GET':
        return render(request, 'login.html')

def store_goals(data):
    goal = Goal(
        goalTitle=data.get("goalTitle"),
        user_id=data.get('userid')
    )
    goal.save()

    for subgoal_data in data.get("subgoals", []):
        print(subgoal_data)
        subgoal = Subgoal(
            goal=goal,
            subgoalTitle=subgoal_data.get("title"),
            timelineDate=subgoal_data.get("timelineDate"),
            timelineTime=subgoal_data.get("timelineTime")
        )
        subgoal.save()

def scan_goals():
    goals_dic = {}
    for goal in Goal.objects.prefetch_related('subgoals').all():  # Use 'subgoals' instead of 'subgoal_set'
        goals_dic[goal.id] = {
            'goalTitle': goal.goalTitle,  # Ensure you're using the correct field name 'goalTitle'
            'completed': goal.completed,
            'subgoals': [
                {
                    'subgoalTitle': subgoal.subgoalTitle,  # Use 'subgoalTitle' as defined in your Subgoal model
                    'timelineDate': subgoal.timelineDate,
                    'timelineTime': subgoal.timelineTime,
                    'completed': subgoal.completed
                } for subgoal in goal.subgoals.all()  # Again, use 'subgoals' to iterate over related Subgoal objects
            ]
        }
    return goals_dic

def dashboard(request):
    if request.method == 'GET':
        goals = scan_goals()
        goals_json = json.dumps(list(goals.values()), cls=DjangoJSONEncoder)
        return render(request, 'dashboard.html', {'goals_json': goals_json})
    elif request.method == 'POST':
        data = json.loads(request.body)
        store_goals(data)
        goals = scan_goals()
        goals_json = json.dumps(list(goals.values()), cls=DjangoJSONEncoder)
        goals_data = json.loads(goals_json)
        return JsonResponse({'goals': goals_data}, status=200)

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