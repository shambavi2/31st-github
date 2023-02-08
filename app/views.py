from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    TFO=TopicForm()
    d={'form':TFO}
    if request.method=='POST':
        fd=TopicForm(request.POST)
        if fd.is_valid():
            tn=fd.cleaned_data['topic_name']
            T=Topic.objects.get_or_create(topic_name=tn)[0]
            T.save()
        return HttpResponse('topic inserted successfully')
        
    return render(request,'insert_topic.html',d)


def webpage_modelform(request):
    WMFD=ModelWebpageForm()
    d={'form':WMFD}
    if request.method=='POST':
        FD=ModelWebpageForm(request.POST)
        if FD.is_valid():
            FD.save()
            return HttpResponse('webpage inserted successfully')
    return render(request,'webpage_modelform.html',d)

def access_modelform(request):
    AMFD=ModelAccess_RecordForm()
    d={'form':AMFD}
    if request.method=='POST':
        FD=ModelAccess_RecordForm(request.POST)
        if FD.is_valid():
            FD.save()
            return HttpResponse('access_record inserted successfully')
    return render(request,'access_modelform.html',d)