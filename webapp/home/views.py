from django.shortcuts import render
from django.shortcuts import HttpResponse
import requests
from .models import restaurant, order, Menu
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, "home/index.html")

def get_takeaway1(request):
    resta = restaurant.objects.all()
    takeaway1 = resta[0].takeaway1
    print(type(takeaway1))
    result = {'takeaway': takeaway1}
    return JsonResponse(result)

def get_ac1(request):
    resta = restaurant.objects.all()
    ac1 = resta[0].ac1
    result = {'ac': ac1}
    return JsonResponse(result)

def get_wifi(request):
    resta = restaurant.objects.all()
    wifi = resta[0].wifi
    result = {'wifi': wifi}
    return JsonResponse(result)

def get_special(request):
    resta = restaurant.objects.get(id=1)
    special = resta.special.dish_name
    result = {'special': special}
    return JsonResponse(result)

def get_payment(request):
    resta = restaurant.objects.all()
    payment = resta[0].payment
    result = {'payment': payment}
    return JsonResponse(result)


def get_veg(request):
    resta = restaurant.objects.all()
    veg = resta[0].veg
    result = {'veg': veg}
    return JsonResponse(result)


def get_can(request):
    resta = restaurant.objects.all()
    can = resta[0].can
    result = {'cancel': can}
    return JsonResponse(result)

def get_washroom(request):
    resta = restaurant.objects.all()
    washroom = resta[0].washroom
    result = {'washroom': washroom}
    return JsonResponse(result)

def get_workinghours(request):
    resta = restaurant.objects.all()
    workinghours = resta[0].workinghours
    result = {'workinghours': workinghours}
    return JsonResponse(result)

def get_Menu(request):
    menu =  Menu.objects.all().values()
    i = 1
    data = []
    for x in menu:
        data.append(x) 
    return JsonResponse(data, safe=False)

def set_order(request):
    dish_name = request.GET['dish_name']
    amount = request.GET['amount']
    spice = request.GET['spice']
    order1 = order(dish_name=dish_name, amount=amount, spice=spice)
    order1.save()
    return HttpResponse('done')

