from TestModel.views import login, homepage, register, dashboard, update_goal_status, update_goal_type, sort_goal, delete_goal, overview, summary, update_subgoal_status
from django.urls import path

urlpatterns = [
    path('login/', login, name='login'),
    path('homepage/', homepage, name='homepage'),
    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('update_goal_status/', update_goal_status, name='update_goal_status'),
    path('update_goal_type/', update_goal_type, name='update_goal_type'),
    path('sort_goal/', sort_goal, name='sort_goal'),
    path('delete_goal/', delete_goal, name='delete_goal'),
    path('overview/', overview, name='overview'),
    path('summary/', summary, name='summary'),
    path('update_subgoal_status/', update_subgoal_status, name='update_subgoal_status'),
    # path('goals/', goals, name = 'goals')
]