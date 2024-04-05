from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Category)
admin.site.register(Product)

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderedItem)
admin.site.register(DeliveryAddress)



admin.site.register(NewCollection)
admin.site.register(WomenCollection)
admin.site.register(MenCollection)
admin.site.register(KidsCollection)
admin.site.register(MotorSportCollection)
admin.site.register(SportCollection)
