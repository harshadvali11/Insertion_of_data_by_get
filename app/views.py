from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse

from django.db.models.functions import Length
from django.db.models import Q,OuterRef,Subquery

def insert_topic(request):
    tn=input('enter topicname')
    TO=Topic.objects.get_or_create(topic_name=tn)
    if TO[1]:
        topics=Topic.objects.all()
        d={'topics':topics}
        return render(request,'display_topics.html',d)
        #return HttpResponse('Topic is Created')
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
        
        d={'webpages':Webpage.objects.all()}
        return render(request,'display_webpages.html',d)
        #return HttpResponse('Webpage is Created')
    else:
        return HttpResponse('Dear User Given Topic is Not Avaialble')


def display_topics(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    return render(request,'display_topics.html',d)

def display_webpages(request):
    webpages=Webpage.objects.all()
    webpages=Webpage.objects.filter(topic_name='Cricket')
    webpages=Webpage.objects.exclude(topic_name='Cricket')
    webpages=Webpage.objects.all()[:5:]
    webpages=Webpage.objects.all()[2:7:1]
    webpages=Webpage.objects.all()[::-1]
    webpages=Webpage.objects.filter(topic_name='Cricket')[:2:]
    webpages=Webpage.objects.all().order_by('name')
    webpages=Webpage.objects.all().order_by('topic_name')
    webpages=Webpage.objects.all().order_by('-name')
    webpages=Webpage.objects.all().order_by(Length('name'))
    webpages=Webpage.objects.all().order_by(Length('name'))
    webpages=Webpage.objects.all().order_by(Length('name').desc())
    webpages=Webpage.objects.all()
    webpages=Webpage.objects.filter(name__startswith='h')
    webpages=Webpage.objects.filter(url__endswith='com')
    webpages=Webpage.objects.filter(name__contains='h')
    webpages=Webpage.objects.filter(name__regex='^h\w+')
    webpages=Webpage.objects.filter(name__in=('Rohit','virat'))
    webpages=Webpage.objects.all()
    webpages=Webpage.objects.filter(Q(name__startswith='h') & Q(url__endswith='in'))
    webpages=Webpage.objects.filter(Q(name__startswith='v') | Q(url__endswith='com'))
    webpages=Webpage.objects.filter(name__startswith='h' , url__endswith='in')
    webpages=Webpage.objects.all()
    #webpages=Topic.objects.annotate(topic_name=Subquery(Webpage.objects.filter(topic_name=OuterRef('pk')).values('name')))[:1]
    webpages=Topic.objects.prefetch_related('webpage_set').all()
    
    
    
    
    d={'webpages':webpages}
    return render(request,'display_webpages.html',d)


def display_access(request):
    access=AccessRecord.objects.all()
    access=AccessRecord.objects.filter(date='2024-10-01')
    access=AccessRecord.objects.all()
    access=AccessRecord.objects.filter(date__gte='2024-10-01')
    access=AccessRecord.objects.filter(date__lte='2024-10-01')
    access=AccessRecord.objects.filter(date__year='2024')
    access=AccessRecord.objects.filter(date__month='10')
    access=AccessRecord.objects.filter(date__day__gt='7')
    
    
    
    d={'access':access}
    return render(request,'display_access.html',d)


def update_webpage(request):
    #where virat their email changing to virat@gmail.com
    #Webpage.objects.filter(name='virat').update(email='virat@gmail.com')

    #where tn is Boxing their url changing to https://Boxing.in
    #Webpage.objects.filter(topic_name='Boxing').update(url='https://Boxing.in')
    
    #Zero rows satisfying condition
    #Webpage.objects.filter(topic_name='Programming').update(url='https://Boxing.in')
    
    #Webpage.objects.filter(pk=6).update(name='Aniket Sharma')
    #Webpage.objects.filter(pk=9).update(topic_name='Hockey')
    
    #Webpage.objects.filter(name='harshad').update(topic_name='Programming')
    #Above Query Gives Error Bcoz
    '''While we r updating Parent Tables Column we should provide the values which 
    are present in Parent Table'''

    #Webpage.objects.update_or_create(name='Hardhik',defaults={'email':'Hardhik@gmail.com'})
    
    #Webpage.objects.update_or_create(topic_name='Boxing',defaults={'email':'Boxing@gmail.com'})
    #Above Query Gives Error Bcoz
    #We cannot Update multiple Rows By using update_or_create method
    
    #Webpage.objects.update_or_create(name='Hardhik',defaults={'topic_name':'Cricket'})
    #Above Query Gives Error Bcoz
    '''While we r updating Parent Tables Column we should provide the 
    Parent Table Object directly'''

    TO=Topic.objects.get(topic_name='Cricket')
    #Webpage.objects.update_or_create(name='Hardhik',defaults={'topic_name':TO})
    
    #Webpage.objects.update_or_create(name='Harshad Vali Shaik',defaults={'topic_name':TO})
   
    Webpage.objects.update_or_create(name='Harshad Vali',defaults={'url':'https:/shaik.in'})
   

    webpages=Webpage.objects.all()
    d={'webpages':webpages}
    return render(request,'display_webpages.html',d)








