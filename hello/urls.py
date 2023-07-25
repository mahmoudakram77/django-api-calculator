from django.urls import include , path

from . import views

urlpatterns = [
    path('django/', views.HelloApi.as_view(), name='hello_api'),
    path('django2/', views.hello_drf, name='hello_api2'),
]
