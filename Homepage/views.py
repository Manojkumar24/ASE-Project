# from django.http import JsonResponse, HttpResponse
# from django.shortcuts import render
from django.shortcuts import redirect

from Manager.models import Food_items,Admin_Image
# from Registration.models import UserProfileInfo, Staffdetails
from Registration.views import *

# , Staff
# from User.models import Order_Food, Order_User
# from django.contrib.auth.models import User


# def populateOrder_Food():
from User.models import Order_User, Order_Food
from eat_at_canteen.forms import *


def default(request):
    user_order_items = []
    if request.user.is_authenticated:
        username = request.user.username
        FoodList = Food_items.objects.all()
        CustomerFoodList = Order_User.objects.all()
        user = User.objects.get(username=username)
        email = user.email
        j = 0
        token = ' '
        for i in CustomerFoodList:
            if i.mailId == email and i.status == 'draft':
                j = 1
                token = i.TokenId
                break
        if j == 1:
            g = Order_Food.objects.filter(Status='dr', TokenId=token)
            for i in g:
                user_order_items.append(i.FoodId.Food_Name)

    if 'breakfast' in request.GET:
        food = Food_items.objects.filter(Category='Tiffin')
    elif 'snack' in request.GET:
        food = Food_items.objects.filter(Category='Snack')
    elif 'starter' in request.GET:
        food = Food_items.objects.filter(Category='Starter')
    else:
        food = Food_items.objects.all()

    contents = {'food': food}
    background = Admin_Image.objects.filter(categories='background')
    canteen_pics = Admin_Image.objects.filter(categories='workplace')
    service_pics = Admin_Image.objects.filter(categories='service')
    if 'employee_id' in request.session:
        user = request.session['employee_id']
        staff = Staffdetails.objects.filter(employee_id=user)
        content1 = {'staff': staff}
        return render(request, 'Homepage/category.html', contents, content1)
    else:
        return render(request, 'Homepage/Homepage.html', {'background': background, 'canteen_pics': canteen_pics, 'service_pics': service_pics, 'food': food})


def search(request):
    template_name = 'Homepage/search.html'
    query = request.POST.get('FoodRequest')
    if query:
        results = Food_items.objects.filter(Food_Name=query).distinct()
    else:
        results = []
    return render(
        request, template_name, {'results': results})

    # return HttpResponse(details)


def itemdetailview(request, pk):
    prod = Food_items.objects.get(Food_id=pk)
    user_order_items = []
    b = item_review.objects.all()

    if request.user.is_authenticated:
        username = request.user.username
        FoodList = Food_items.objects.all()
        CustomerFoodList = Order_User.objects.all()
        user = User.objects.get(username=username)
        email = user.email

        j = 0
        token = ' '
        for i in CustomerFoodList:
            if i.mailId == email and i.status == 'draft':
                j = 1
                token = i.TokenId
                break
        if j == 1:
            g = Order_Food.objects.filter(Status='dr', TokenId=token)
            for i in g:
                user_order_items.append(i.FoodId.Food_Name)
    j = 0
    for i in b:
        if i.product == prod:
            j = 1
            break
    if j == 1:
        list = item_review.objects.filter(product=prod).order_by('latest_pub_date')
    else:
        list = []
    s = None
    if prod.rating > 0:
        s = str(prod.rating)
    listnew = []

    contents = {'prod': prod, 'user_items': user_order_items, 'list': list, 's': s}
    return render(request, 'Homepage/itemdetail.html', contents)


@login_required
def reviewtext(request, pk):
    prod = Food_items.objects.get(Food_id=pk)
    if request.method == 'POST':
        form = writereview(request.POST)
        if form.is_valid():
            j = 0
            content = request.POST.get('content')
            rating = request.POST.get('ratingnew')
            d = item_review.objects.all()
            for i in d:
                if i.customer == request.user and i.product == prod:
                    i.rating = rating
                    i.content = content
                    j = 1
                    i.save()
            if j == 0:
                newreview = item_review.objects.create(product=prod, customer=request.user, content=content,
                                                       rating=rating)
                newreview.save()

            prod.rating = ((prod.rating * prod.No_of_reviews) + int(rating)) / (prod.No_of_reviews + 1)
            prod.rating = round(prod.rating, 1)
            prod.No_of_reviews = prod.No_of_reviews + 1
            prod.save()
            return redirect('/' + str(pk) + '/')
    else:
        form = writereview()
    return render(request, 'Homepage/writereview.html', {'form': form})
