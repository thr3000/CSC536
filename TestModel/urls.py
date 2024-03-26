from TestModel.views import register, testdb, homepage, login, dashboard
from django.urls import path

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name = 'login'),
    path('testdb/', testdb, name='testdb'),
    path('homepage/',homepage, name ='homepage'),
    path('dashboard/',dashboard, name='dashboard'),
]