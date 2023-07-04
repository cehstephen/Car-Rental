from django.contrib import admin

from .models import Car, CarType, BatteryType, EngineType, ServiceCriteria, AllCarsNeedingServicing
# Register your models here.

admin.site.register(Car)
admin.site.register(CarType)
admin.site.register(BatteryType)
admin.site.register(EngineType)
admin.site.register(ServiceCriteria)
admin.site.register(AllCarsNeedingServicing)
