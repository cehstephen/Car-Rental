from django.urls import path

from .apiviews import CarList, CheckCars, EngineTypeList, BatteryTypeList, ServiceCriteriaList, CarDetail, CarTypeList, CarsNeedingServicing, UserCreate, UserLogin


urlpatterns = [
    path("users/create", UserCreate.as_view(), name="users_create"),
    path("login", UserLogin.as_view(), name="login"),
    path("cars", CarList.as_view(), name="cars"),
    path("engines", EngineTypeList.as_view(), name="engines"),
    path("battery", BatteryTypeList.as_view(), name="batteries"),
    path("car_type", CarTypeList.as_view(), name="cartypes"),
    path("need_servicing", CarsNeedingServicing.as_view(), name="need_servicing"),
    path("service_criteria", ServiceCriteriaList.as_view(), name="service_criteria"),
    path("check/cars", CheckCars.as_view(), name="check_cars"),
    path("cars/<int:pk>/details", CarDetail.as_view(), name="car_details"),
]
