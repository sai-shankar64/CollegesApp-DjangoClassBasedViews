import os,sys,django
os.environ['DJANGO_SETTINGS_MODULE'] = os.getcwd().split("\\")[-1]+'.settings'
django.setup()

from onlineapp.models import *
from onlineapp.views import *
manager=College.objects
# print(type(manager).__name__)
# print(type(College.objects.all()[0]).__name__)
# querysets=College.objects.all()
# print(type(querysets).__name__)
# print(querysets)
# for queryset in querysets:
#     print(type(queryset).__name__,queryset)

# print(testview("nothing"))