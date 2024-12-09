from django.contrib import admin
from .models import restaurant, Menu, order
# Register your models here.

admin.site.register(restaurant)
admin.site.register(Menu)
admin.site.register(order)