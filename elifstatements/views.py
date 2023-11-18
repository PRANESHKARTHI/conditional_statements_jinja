from django.shortcuts import render

# Create your views here.
def elifstatements(request):
    d={"a":11, "b":10 , "c":12}
    return render(request,"elifstatements.html",d)