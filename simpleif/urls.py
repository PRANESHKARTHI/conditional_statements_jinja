from django.urls import path
from simpleif.views import *
app_name="anything"
urlpatterns=[
    path('simpleif/',simpleif,name="simpleif"),
]