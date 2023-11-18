from django.shortcuts import render

# Create your views here.
def nestedif(request):
    d={"a":10,"b":20,"c":20}
    return render(request,"nestedif.html",d)