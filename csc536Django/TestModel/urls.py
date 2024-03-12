from TestModel.views import login, testdb
from django.urls import path

urlpatterns = [
    path('login/', login, name='login'),
    path('testdb/', testdb, name='testdb'),
]