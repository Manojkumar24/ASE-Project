from django.shortcuts import render
import json
# Create your views here.
from django.http import HttpResponse
from history.models import foodorders,new1
#global dict1
import datetime



def history(request):
    return render(request,'history/history.html',{'title':'history'})

def users(request):
    dict1={}
    if request.method == 'POST':
        Fromdate = request.POST.get('Fromdate')
        Todate = request.POST.get('Todate')
        print(Fromdate)
        x=int(Fromdate[0:4])
        x1=int(Fromdate[5:7])
        x2=int(Fromdate[8:10])
        y=int(Todate[0:4])
        y1=int(Todate[5:7])
        y2=int(Todate[8:10])



        all_foodorders=foodorders.objects.all();


        for fo in all_foodorders:
            z=fo.date.isoformat()
            z1=int(z[0:4])
            z2=int(z[5:7])
            z3=int(z[8:10])
            if z1>=x and z1<=y:
                if z2>=x1 and z2<=y1:
                    if z3>=x2 and z3<=y2:
                        dict1[fo.foodname]=0;
        for fo in all_foodorders:
            a=fo.date.isoformat()
            z4=int(a[0:4])
            z5=int(a[5:7])
            z6=int(a[8:10])
            if z4>=x and z4<=y:
                if z5>=x1 and z5<=y1:
                    if z6>=x2 and z6<=y2:

                       dict1[fo.foodname]=dict1[fo.foodname]+fo.quantity;

        print(dict1)
        emp=new1.objects.all()
        emp.delete()
        for key,value in dict1.items():
            print(key,value)
            p=new1(item=key,frequency=value)
            p.save()


    return render(request,'history/history.html',context={'d':dict1})
