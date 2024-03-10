# import os
# from django.db import connection
#
# os.environ['DJANGO_SETTINGS_MODULE'] = 'csc536Django.settings'
# curson = connection.cursor


from django.http import HttpResponse

from TestModel.models import Goals
def testdb(request):
    goals = Goals(create_date='2024.3.10', content='finish proposal')
    goals.save()
    return HttpResponse("<p>a new goal finish proposal is added successfully</p>")
