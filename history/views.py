from django.shortcuts import render
from django.http import HttpResponse
from history.models import new1,new2
import datetime
from User.models import  Order_Food

def users(request):
    return render(request,'history/history.html')
def datespliting(Fromdate):
    a=int(Fromdate[0:4])
    a1=int(Fromdate[5:7])
    a2=int(Fromdate[8:10])
    return a,a1,a2
def users1(request):
    dict1={}
    if request.method=='POST':
        Fromdate = request.POST.get('fromdate')
        Todate = request.POST.get('todate')
        year1,month1,date1=datespliting(Fromdate);
        year2,month2,date2=datespliting(Todate);
        all_foodorders=Order_Food.objects.all();
        for fo in all_foodorders:
            z=fo.date.isoformat()
            year3,month3,date3=datespliting(z);
            if year3>=year1 and year3<=year2:
                if month3>=month1 and month3<=month2:
                    if date3>=date1 and date3<=date2:
                        dict1[fo.FoodId]=0;

        for fo in all_foodorders:
            a4=fo.date.isoformat()
            year4,month4,date4=datespliting(a4);
            if year4>=year1 and year4<=year2:
                if month4>=month1 and month4<=month2:
                    if date4>=date1 and date4<=date2:

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
            year5,month5,date5=datespliting(fromdate);
            year6,month6,date6=datespliting(todate);

            all_foodorders=Order_Food.objects.filter(Status='conf');
            for i in all_foodorders:
              m=i.date.isoformat()
              year7,month7,date7=datespliting(m);
              if year7>=year5 and year7<=year6:
                  if month7>=month5 and month7<=month6:
                      if date7>=date5 and date7<=date6:
                              t=i.date.isoformat();
                              dict2[t]=0;

            for i in all_foodorders:
              b4=i.date.isoformat()
              year8,month8,date8=datespliting(b4)
              if year8>=year5 and year8<=year6:
                  if month8>=month5 and month8<=month6:
                      if date8>=date5 and date8<=date6:
                         t=i.date.isoformat()
                         dict2[t]=i.price;
            new2.objects.all().delete()

            for key,value in dict2.items():
               print(key,value)
               p1=new2(Date=key,price=value)
               p1.save()



            print(dict2)
       return render(request,'history/history1.html',context={'d1':dict2})

def test(request):
           return render(request,'history/test.html')
