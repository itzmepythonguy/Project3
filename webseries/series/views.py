from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import webseries
from. forms import seriesform

# Create your views here.
def Home(request):
    series=webseries.objects.all()
    return render(request,'index.html',{'series':series})
def web(request,web_id):
    webs=webseries.objects.get(id=web_id)
    return render(request,'detials.html',{'web':webs})
def add(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        year=request.POST.get('year',)
        desc=request.POST.get('desc',)
        img=request.FILES['img']
        series= webseries(name=name,year=year,desc=desc,img=img)
        series.save();
    return render(request,'add.html')
def update(request,web_id):
    series1 = webseries.objects.get(id=web_id)
    form=seriesform(request.POST or None,request.FILES,instance=series1)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'series':series1})

def delete(request,id):
    if request.method=='POST':
        series2= webseries.objects.get(id=id)
        series2.delete()
        return redirect('/')
    return render(request,'delete.html')

