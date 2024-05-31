
from django.shortcuts import render
from surprise.models import Message, Image
from datetime import datetime



# Renders the html
# request: passed from view
# d: datetime object
# n: number of day, as a string
def renderHTML(request, d, n):
    context = {}
    if datetime.now() < d:
        context = {'time': d.strftime("%I:%M%p on %B %d")}
        return render(request, "error.html", context)
    context = {
        'message': Message.objects.get(day=n).content,
        'images': '</br>'.join(['<img src=%s>' % img.upload.url for img in Image.objects.filter(day=n)])
    }
    return render(request, "index.html", context)

# Create your views here.
def firstday(request):
    return renderHTML(request, datetime(2024,5,2,11,0), "1")

def secondday(request):
    return renderHTML(request, datetime(2024,5,6,11,0), "2")

def thirdday(request):
    return renderHTML(request, datetime(2024,5,10,11,0), "3")

def fourthday(request):
    return renderHTML(request, datetime(2024,5,14,11,0), "4")
