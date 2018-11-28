from django.shortcuts import render
from . import form
from .models import Food_items, Dining_Tables, Available_Towns
from django.core.mail import send_mail
from django.conf import settings
from User.models import Order_Food, Order_User
from homedelivery.models import HD_Address


# Create your views here.
def index(request, content=None):
    user_order_item = Order_User.objects.filter(status='ordered')
    user_pre_item = Order_User.objects.filter(status='in Preparation')
    user_conorder_item = Order_User.objects.filter(status='User Conform')
    if content:
        content['user_order_item'] = user_order_item
        content['user_pre_item'] = user_pre_item
        content['user_conorder_item'] = user_conorder_item
    else:
        content = {'user_order_item': user_order_item, 'user_pre_item': user_pre_item, 'user_conorder_item': user_conorder_item}
    return render(request, 'Manager/index.html', content)


def add_food(request):
    f1 = form.Add_food()
    error = None
    if request.method == 'POST':
        f1 = form.Add_food(request.POST, request.FILES)
        if f1.is_valid():
            fid = f1.cleaned_data['Id']
            name = f1.cleaned_data['Name']
            price = f1.cleaned_data['Price']
            qu = f1.cleaned_data['Quantity']
            category = f1.cleaned_data['Category']
            try:
                img = f1.cleaned_data['image']
                try:
                    Food_items.objects.create(Food_id=fid, Food_Name=name, Food_Price=price, image=img, quantity=qu,
                                              Category=category)
                except:
                    error = 'Unable to Add the food item'
            except:
                try:
                    Food_items.objects.create(Food_id=fid, Food_Name=name, Food_Price=price, quantity=qu,
                                              Category=category)
                except:
                    error = 'Unable to Add the food item'
            item = Food_items.objects.all()
            if error:
                content = {'item': item, 'error': error}
            else:
                content = {'item': item}
            return render(request, 'Manager/Food_home.html', content)
    return render(request, 'Manager/Add_food.html', {'form': f1})


def remove_food(request):
    f2 = form.get_id()
    if request.method == 'POST':
        f2 = form.get_id(request.POST)
        if f2.is_valid():
            fid = f2.cleaned_data['Id']
            try:
                f_item = Food_items.objects.get(Food_id__exact=fid)
                f_item.delete()
            except:
                pass
        item = Food_items.objects.all()
        content = {'item': item}
        return render(request, 'Manager/Food_home.html', content)
    item = Food_items.objects.all()
    content = {'form': f2, 'item': item}
    return render(request, 'Manager/Remove_food.html', content)


def update_food(request, f_id=None):
    if f_id != 0:
        try:
            update = Food_items.objects.get(Food_id=f_id)
            content = {'update': update}
            return render(request, 'Manager/Update_food.html', content)
        except:
            error = "Invalid FoodID"
            item = Food_items.objects.all()
            content = {'item': item, 'error': error}
            return render(request, 'Manager/Update_food.html', content)
    else:
        item = Food_items.objects.all()
        content = {'item': item}
        return render(request, 'Manager/Update_food.html', content)


def check_update_food(request):
    if request.method == "POST":
        f_id = request.POST['Id']
        name = request.POST['Name']
        price = request.POST['Price']
        qu = request.POST['Quantity']
        category = request.POST['Category']
        food_temp = Food_items.objects.get(Food_id=f_id)
        food_temp.Food_Name = name
        food_temp.Food_Price = price
        food_temp.quantity = qu
        food_temp.Category = category
        try:
            img = request.FILES['image']
            if img != None and img != food_temp.image:
                food_temp.image.delete()
                food_temp.image = img
                food_temp.save()
            else:
                food_temp.image = img
                food_temp.save()
        except:
            food_temp.save()
    item = Food_items.objects.all()
    content = {'item': item}
    return render(request, 'Manager/Update_food.html', content)


def food_home(request):
    item = Food_items.objects.all()
    content = {'item': item}
    return render(request, 'Manager/Food_home.html', content)


def tables_home(request):
    item = Dining_Tables.objects.all()
    content = {'item': item}
    return render(request, 'Manager/tables_home.html', content)


def remove_tables(request):
    f2 = form.get_id()
    if request.method == 'POST':
        f2 = form.get_id(request.POST)
        if f2.is_valid():
            fid = f2.cleaned_data['Id']
            try:
                Dining_Tables.objects.get(Table_id__exact=fid).delete()
            except:
                pass
            return render(request, 'Manager/tables_home.html')
    item = Dining_Tables.objects.all()
    content = {'form': f2, 'item': item}
    return render(request, 'Manager/Remove_table.html', content)


def add_tables(request):
    f1 = form.Add_tables()
    error = None
    if request.method == 'POST':
        f1 = form.Add_tables(request.POST)
        if f1.is_valid():
            fid = f1.cleaned_data['Id']
            availabilty = f1.cleaned_data['availability']
            size = f1.cleaned_data['size']
            zone = f1.cleaned_data['zone']
            try:
                Dining_Tables.objects.create(Table_id=fid, availability=availabilty, size=size, zone=zone)
            except:
                error = "Table Id Already Exits"
            item = Dining_Tables.objects.all()
            if error:
                content = {'item': item, 'error': error}
            else:
                content = {'item': item}
            return render(request, 'Manager/tables_home.html', content)
    return render(request, 'Manager/Add_tables.html', {'form': f1})


def town_home(request):
    item = Available_Towns.objects.all()
    content = {'item': item}
    return render(request, 'Manager/town_home.html', content)


def remove_towns(request):
    f2 = form.Remove_city()
    if request.method == 'POST':
        f2 = form.Remove_city(request.POST)
        if f2.is_valid():
            fname = f2.cleaned_data['town']
            try:
                Available_Towns.objects.get(Towns__exact=fname).delete()
            except:
                pass
            return render(request, 'Manager/town_home.html')
    item = Available_Towns.objects.all()
    content = {'form': f2, 'item': item}
    return render(request, 'Manager/Remove_town.html', content)


def add_towns(request):
    f1 = form.Add_city()
    error = None
    if request.method == 'POST':
        f1 = form.Add_city(request.POST)
        if f1.is_valid():
            fname = f1.cleaned_data['town']
            pincode = f1.cleaned_data['pincode']
            try:
                Available_Towns.objects.create(Towns=fname, pincode=pincode)
            except:
                error = 'Town already exists'
            if error:
                item = Available_Towns.objects.all()
                content = {'item': item, 'error': error}
                return render(request, 'Manager/town_home.html', content)
            else:
                item = Available_Towns.objects.all()
                content = {'item': item}
                return render(request, 'Manager/town_home.html', content)
    return render(request, 'Manager/Add_town.html', {'form': f1})


def check_update_table(request):
    error = None
    if request.method == "POST":
        f_id = request.POST['Id']
        ava = request.POST['availability']
        size = request.POST['size']
        zone = request.POST['zone']
        table_temp = Dining_Tables.objects.get(Table_id=f_id)
        table_temp.availability = ava
        table_temp.size = size
        table_temp.zone = zone
        try:
            table_temp.save()
        except:
            error = 'Unable to update'
        item = Dining_Tables.objects.all()
        if error:
            content = {'item': item, 'error': error}
        else:
            content = {'item': item}
        return render(request, 'Manager/Update_tables.html', content)
    else:
        item = Dining_Tables.objects.all()
        content = {'item': item}
        return render(request, 'Manager/Update_tables.html', content)


def update_table(request, id=None):
    if id != 0:
        try:
            update = Dining_Tables.objects.get(Table_id=id)
            content = {'update': update}
            return render(request, 'Manager/Update_tables.html', content)
        except:
            error = 'TableId not found'
            item = Dining_Tables.objects.all()
            content = {'item': item, 'error': error}
            return render(request, 'Manager/Update_tables.html', content)
    else:
        item = Dining_Tables.objects.all()
        content = {'item': item}
        return render(request, 'Manager/Update_tables.html', content)


def list_items(request, id=None):
    if id:
        try:
            items = Order_Food.objects.filter(TokenId=id)
            content = {'items': items}
            return render(request, 'Manager/list_items.html', content)
        except:
            pass
    index_content = {'error': 'Invalid TokenId'}
    return index(request, index_content)


def send_email(request, t_id=None):
    msg = 'Email is not sent'
    if t_id:
        if request.method == 'POST':
            item = Order_User.objects.get(TokenId__exact=t_id)
            email = item.mailId
            time = request.POST['time']
            subject = 'Your order expected time is' + time
            body = '''Dear User,
            You order with Token Id ''' + t_id + ''' is expected to be done by ''' + time + ''' 
            Thank You for ordering'''
            try:
                send_mail(subject, body, settings.EMAIL_HOST_USER, [email], fail_silently=True)
                msg = 'Email is sent'
                item.status = 'in Preparation'
                item.save()
            except:
                pass
    user_order_item = Order_User.objects.filter(status='ordered')
    user_pre_item = Order_User.objects.filter(status='in Preparation')
    content = {'user_order_item': user_order_item, 'user_pre_item': user_pre_item, 'msg': msg}
    return render(request, 'Manager/index.html', content)


def change_status(request, f_id=None):
    error = 'Invalid TokenId'
    if f_id:
        try:
            items = Order_Food.objects.filter(TokenId=f_id)
            add = HD_Address.objects.get(tokenId__TokenId=f_id)
            content = {'items': items, 'add': add}
        except:
            items = Order_Food.objects.filter(TokenId=f_id)
            content = {'items': items}
        status = Order_User.objects.filter(TokenId=f_id).first().status
        content['status'] = status
        return render(request, 'Manager/change_status.html', content)
    user_order_item = Order_User.objects.filter(status='ordered')
    user_pre_item = Order_User.objects.filter(status='in Preparation')
    content = {'user_order_item': user_order_item, 'user_pre_item': user_pre_item, 'error': error}
    return render(request, 'Manager/index.html', content)


def send_com_email(request, t_id=None):
    msg = 'Email is not sent'
    if t_id:
        if request.method == 'POST':
            item = Order_User.objects.get(TokenId__exact=t_id)
            email = item.mailId
            status = request.POST['Completed']
            body = '''Dear User,
            You order with Token Id ''' + t_id + ''' is completed with its progess. We hope you will enjoy the food 
            Thank You'''
            if item.status == 'User Conform':
                subject = 'Delivery Conformed'
            else:
                subject = 'Your order is ready'
            try:
                send_mail(subject, body, settings.EMAIL_HOST_USER, [email], fail_silently=True)
                msg = 'Email is sent'
                item.status = status
                item.save()
            except:
                pass
    user_order_item = Order_User.objects.filter(status='ordered')
    user_pre_item = Order_User.objects.filter(status='in Preparation')
    content = {'user_order_item': user_order_item, 'user_pre_item': user_pre_item, 'msg': msg}
    return render(request, 'Manager/index.html', content)


def send_home_email(request, t_id=None):
    msg = 'Email is not sent'
    if t_id:
        if request.method == 'POST':
            item = Order_User.objects.get(TokenId__exact=t_id)
            email = item.mailId
            status = request.POST['in Delivery']
            subject = 'Your order status: ' + status
            body = '''Dear User,
                    You order with Token Id ''' + t_id + ''' is changed its status to ''' + status + ''' You will receive your food soon.  
                    Thank You for ordering'''
            try:
                send_mail(subject, body, settings.EMAIL_HOST_USER, [email], fail_silently=True)
                msg = 'Email is sent'
                item.status = status
                item.save()
            except:
                pass
    user_order_item = Order_User.objects.filter(status='ordered')
    user_pre_item = Order_User.objects.filter(status='in Preparation')
    content = {'user_order_item': user_order_item, 'user_pre_item': user_pre_item, 'msg': msg}
    return render(request, 'Manager/index.html', content)