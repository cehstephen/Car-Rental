from django.db import models

# Create your models here.


class ServiceCriteria(models.Model):
    name = models.CharField(max_length=100, blank=False)
    due = models.IntegerField(blank=False)
    
    def __str__(self):
        return self.name


class BatteryType(models.Model):
    name = models.CharField(max_length=100, blank=False)
    service_criteria = models.ForeignKey(ServiceCriteria, related_name='batterytype', on_delete=models.DO_NOTHING)
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Battery(models.Model):
    name = models.CharField(max_length=100, blank=False)
    type = models.ForeignKey(BatteryType, related_name='type', on_delete=models.DO_NOTHING)
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class EngineType(models.Model):
    name = models.CharField(max_length=50, blank=False)
    service_criteria = models.ForeignKey(ServiceCriteria, related_name='enginetype', on_delete=models.DO_NOTHING)
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CarType(models.Model):
    name = models.CharField(max_length=50, blank=False)
    engine = models.ForeignKey(EngineType, related_name='engine', on_delete=models.DO_NOTHING)
    battery = models.ForeignKey(BatteryType, related_name='battery', on_delete=models.DO_NOTHING)
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Car(models.Model):
    name = models.CharField(max_length=50, blank=False)
    car_type = models.ForeignKey(CarType, on_delete=models.DO_NOTHING)
    last_battery_service_date = models.DateField(auto_now=True, editable=True)
    current_millage = models.IntegerField(blank=False, default=0)
    last_serviced_millage = models.IntegerField(blank=True, default=0)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class AllCarsNeedingServicing(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    due = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=100, blank=True)
    serviced = models.BooleanField(default=False)
    date_serviced = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(auto_now=True)
