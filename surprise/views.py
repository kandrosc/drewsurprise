
from django.shortcuts import render
from surprise.models import Message, Image
from datetime import datetime



# Renders the html
# request: passed from view
# date: datetime object
# num: number of day, as a string
# background: url of background to use
def renderHTML(request, date, num, background):
    context = {}
    if datetime.now() < date:
        context = {'time': date.strftime("%I:%M%p on %B %d")}
        return render(request, "error.html", context)
    context = {
        'message': Message.objects.get(day=num).content,
        'images': '</br>'.join(['<img src=%s style="width:600px;height:400px;">' % img.upload.url for img in Image.objects.filter(day=num)]),
        'background': background
    }
    return render(request, "index.html", context)

# Create your views here.
def firstday(request):
    return renderHTML(request, datetime(2024,5,2,11,0), "1", '/media/backgrounds/one.gif')

def secondday(request):
    return renderHTML(request, datetime(2024,5,6,11,0), "2", '/media/backgrounds/one.gif')

def thirdday(request):
    return renderHTML(request, datetime(2024,5,10,11,0), "3", '/media/backgrounds/one.gif')

def fourthday(request):
    return renderHTML(request, datetime(2024,5,14,11,0), "4", '/media/backgrounds/one.gif')
