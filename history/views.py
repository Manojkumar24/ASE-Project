from django.shortcuts import render
from django.http import HttpResponse
from history.models import new1,new2
import datetime
from User.models import  Order_Food

def users(request):
    return render(request,'history/history.html')


def users1(request):
    dict1={}
    if request.method=='POST':
        Fromdate = request.POST.get('Fromdate')
        Todate = request.POST.get('Todate')


        x=int(Fromdate[0:4])
        x1=int(Fromdate[5:7])
        x2=int(Fromdate[8:10])
        y=int(Todate[0:4])
        y1=int(Todate[5:7])
        y2=int(Todate[8:10])
        all_foodorders=Order_Food.objects.filter(Status='conf');







        for fo in all_foodorders:
            z=fo.date.isoformat()
            z1=int(z[0:4])
            z2=int(z[5:7])
            z3=int(z[8:10])
            if z1>=x and z1<=y:
                if z2>=x1 and z2<=y1:
                    if z3>=x2 and z3<=y2:
                        dict1[fo.FoodId]=0;

        for fo in all_foodorders:
            a4=fo.date.isoformat()
            z4=int(a4[0:4])
            z5=int(a4[5:7])
            z6=int(a4[8:10])
            if z4>=x and z4<=y:
                if z5>=x1 and z5<=y1:
                    if z6>=x2 and z6<=y2:

                       dict1[fo.FoodId]=dict1[fo.FoodId]+fo.quantity;



        emp=new1.objects.all()
        emp.delete()
        for key,value in dict1.items():
            print(key,value)
            p=new1(item=key,frequency=value)
            p.save()

    return render(request,'history/history2.html',context={'d':dict1})
def users2(request):
       dict2={}
       if request.method=='POST':
            fromdate=request.POST.get('fromdate')
            todate=request.POST.get('todate')
            a=int(fromdate[0:4])
            a1=int(fromdate[5:7])
            a2=int(fromdate[8:10])
            b=int(todate[0:4])
            b1=int(todate[5:7])
            b2=int(todate[8:10])
            all_foodorders=Order_Food.objects.filter(Status='conf');


            for i in all_foodorders:
              m=i.date.isoformat()
              print(m)
              m1=int(m[0:4])
              m2=int(m[5:7])
              m3=int(m[8:10])
              if m1>=a and m1<=b:
                  if m2>=a1 and m2<=b1:
                      if m3>=b2 and m3<=b:
                              t=i.date.isoformat();
                              dict2[t]=0;

            for i in all_foodorders:
              b4=i.date.isoformat()
              m4=int(b4[0:4])
              m5=int(b4[5:7])
              m6=int(b4[8:10])
              if m4>=a and m4<=b:
                  if m5>=a1 and m5<=b1:
                      if m6>=a2 and m6<=b2:
                         t=i.date.isoformat()
                         print(t)
                         print(type(t));
                         dict2[t]=i.price;


            emp2=new2.objects.all()
            emp2.delete()

            for key,value in dict2.items():
               print(key,value)
               p1=new2(Date=key,price=value)
               p1.save()



            print(dict2)
       return render(request,'history/history1.html',context={'d1':dict2})
