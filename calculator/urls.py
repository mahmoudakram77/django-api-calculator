from django.urls import path ,re_path , include
from .views import CalculatorView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'calculator', CalculatorView , 'calculator')

urlpatterns = [
    path('api/', include(router.urls))
]
