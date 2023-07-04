from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from .models import CarType, Car, BatteryType, EngineType, ServiceCriteria, AllCarsNeedingServicing


class BatteryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BatteryType
        fields = '__all__'


class EngineTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngineType
        fields = '__all__'


class SerivceCriteriaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ServiceCriteria
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Car
        fields = '__all__'


class CarTypeSerializer(serializers.ModelSerializer):
    car = CarSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = CarType
        fields = '__all__'


class AllCarsNeedingServicingSeializer(serializers.ModelSerializer):
    #current_millage = serializers.ReadOnlyField(source='car.current_millage')
    #last_battery_service_date = serializers.ReadOnlyField(source='car.last_battery_service_date')
    car = serializers.ReadOnlyField(source='car.car_type')

    class Meta:
        model = AllCarsNeedingServicing
        #read_only_fields = ('current_millage', 'last_battery_service_date', 'car_type')
        fields = "__all__" #('id', 'last_serviced_millage', 'car', 'current_millage', 'last_battery_service_date', 'car_type')

    # def create(self, validated_data):
    #     cars_needing_service = AllCarsNeedingServicing(
    #         car = validated_data.car,
    #         engine_name = validated_data.engine_name,
    #         battary_name = validated_data.battary_name,
    #         battary_service_every = validated_data.battary_service_every,
    #         engine_service_every = validated_data.engine_service_every,
    #         current_millage = validated_data.current_millage,
    #         last_serviced_millage = validated_data.last_serviced_millage,
    #         last_battery_service_date = validated_data.last_battery_service_date,
    #     )
        
    #     cars_needing_service.save()
    #     return cars_needing_service

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password")
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User(
            username = validated_data['username'],
            email = validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user