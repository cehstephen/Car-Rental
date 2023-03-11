from rest_framework import generics
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .serializers import CarSerializer, EngineTypeSerializer, BatteryTypeSerializer, SerivceCriteriaSerializer, CarTypeSerializer, AllCarsNeedingServicingSeializer, UserSerializer
from .models import Car, CarType, EngineType, BatteryType, ServiceCriteria, AllCarsNeedingServicing

class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class ServiceCriteriaList(generics.ListCreateAPIView):
    queryset = ServiceCriteria.objects.all()
    serializer_class = SerivceCriteriaSerializer


class EngineTypeList(generics.ListCreateAPIView):
    queryset = EngineType.objects.all()
    serializer_class = EngineTypeSerializer


class CarTypeList(generics.ListCreateAPIView):
    queryset = CarType.objects.all()
    serializer_class = CarTypeSerializer


class BatteryTypeList(generics.ListCreateAPIView):
    queryset = BatteryType.objects.all()
    serializer_class = BatteryTypeSerializer


class CarDetail(generics.RetrieveDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarsNeedingServicing(generics.ListAPIView):
    def get_queryset(self):
        #engine_service_criteria = Car.car_type.engine.service_criteria
        queryset = Car.objects.filter(current_millage__gte = 20000)
        return queryset
    serializer_class = CarSerializer


class  CheckCars(generics.ListAPIView):
    def get_queryset(self):
        allcars = Car.objects.select_related('car_type').filter(car_type__engine__name="Capulet Engine")

        #engine = item.
        queryset = allcars #AllCarsNeedingServicing.objects.filter()
        #Car.objects.select_related("car_type__engine").filter(current_millage__gte = 20000)
        return queryset
    serializer_class = CarSerializer #AllCarsNeedingServicingSeializer


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

class UserLogin(APIView):
    permission_classes = ()

    def post(self, request,):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong credentials"}, status=status.HTTP_400_BAD_REQUEST)


"""
Django filter documentation
===========================

Greater than:

Person.objects.filter(age__gt=20)
Greater than or equal to:

Person.objects.filter(age__gte=20)
Less than:

Person.objects.filter(age__lt=20)
Less than or equal to:

Person.objects.filter(age__lte=20)
You can find them all in [the documentation].(https://docs.djangoproject.com/en/stable/ref/models/querysets/).

"""