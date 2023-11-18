from django.urls import path
from nestedif.views import *
app_name="something"
urlpatterns=[
    path('nestedif/',nestedif,name="nestedif"),
]