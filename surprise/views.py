from django.shortcuts import render
from datetime import datetime

# Create your views here.
def firstday(request):
    context = {}
    d = datetime(2024,6,2,11,0)
    if datetime.now() < d:
        context = {'time': d.strftime("%m/%d/%Y, %I:%M%p")}
        return render(request, "error.html", context)
    return render(request, "firstday.html", context)

def secondday(request):
    context = {}
    d = datetime(2024,6,9,11,0)
    if datetime.now() < d:
        context = {'time': d.strftime("%m/%d/%Y, %I:%M%p")}
        return render(request, "error.html", context)
    return render(request, "secondday.html", context)

def thirdday(request):
    context = {}
    d = datetime(2024,6,16,11,0)
    if datetime.now() < d:
        context = {'time': d.strftime("%m/%d/%Y, %I:%M%p")}
        return render(request, "error.html", context)
    return render(request, "thirdday.html", context)