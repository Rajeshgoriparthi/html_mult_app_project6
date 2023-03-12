from app1.views import *
from django.urls import path
app_name='sample'
urlpatterns=[
    path('Mom/',Mom,name='Mom'),
]