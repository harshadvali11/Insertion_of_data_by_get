from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse

def insert_topic(request):
    tn=input('enter topicname')
    TO=Topic.objects.get_or_create(topic_name=tn)
    if TO[1]:
        return HttpResponse('Topic is Created')
    else:
        return HttpResponse('Topic is already Exists')

'''
def insert_webpage(request):
    tn=input('enter tn')
    n=input('enter name')
    u=input('enter url')
    e=input('enter email')

    TO=Topic.objects.get_or_create(topic_name=tn)[0]

    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)

    if WO[1]:
        return HttpResponse('Webapge is Created')
    else:
        return HttpResponse('Webpage is Already Exists')
        
'''
'''
def insert_webpage(request):
    tn=input('enter tn')
    n=input('enter name')
    u=input('enter url')
    e=input('enter email')

    TO=Topic.objects.get(topic_name=tn)

    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]

    return HttpResponse('Webpage is cReated')
'''

def insert_webpage(request):
    tn=input('enter tn')
    n=input('enter name')
    u=input('enter url')
    e=input('enter email')

    QLTO=Topic.objects.filter(topic_name=tn)
    if QLTO:
        TO=QLTO[0]
        WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)
        return HttpResponse('Webpage is Created')
    else:
        return HttpResponse('Dear User Given Topic is Not Avaialble')













