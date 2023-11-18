from django.urls import path
from elifstatements.views import *
app_name="anything"
urlpatterns=[
    path('elifstatements/',elifstatements,name="elifstatements"),
]