from TestModel.views import login, homepage, register, dashboard
from django.urls import path

urlpatterns = [
    path('login/', login, name='login'),
    path('homepage/', homepage, name='homepage'),
    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    # path('goals/', goals, name = 'goals')
]