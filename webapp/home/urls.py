from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('takeaway', views.get_takeaway1, name='takeaway1'),
    path('ac', views.get_ac1, name='ac1'),
    path('wifi', views.get_wifi, name='wifi'),
    path('special', views.get_special, name='special'),
    path('payment', views.get_payment, name='payment'),
    path('veg', views.get_veg, name='veg'),
    path('cancel', views.get_can, name='cancel'),
    path('washroom', views.get_washroom, name='washroom'),
    path('workinghours', views.get_workinghours, name='workinghours'),
    path('menu', views.get_Menu, name='menu'),
    path('order', views.set_order, name='order'),
]