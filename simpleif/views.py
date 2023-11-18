from django.shortcuts import render

# Create your views here.
def simpleif(request):
    d={"a":11}
    return render(request,"simpleif.html",d)