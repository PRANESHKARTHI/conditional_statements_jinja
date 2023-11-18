from django.urls import path
from ifelse.views import *
app_name="anything"
urlpatterns=[
    path('ifelse/',ifelse,name="ifelse"),
]