from TestModel.views import login, homepage, register, dashboard, update_goal_status
from django.urls import path

urlpatterns = [
    path('login/', login, name='login'),
    path('homepage/', homepage, name='homepage'),
    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('update_goal_status/', update_goal_status, name='update_goal_status')
    # path('goals/', goals, name = 'goals')
]