from app2.views import *
from django.urls import path
app_name='sample'
urlpatterns=[
    path('Dad/',Dad,name='Dad'),
]