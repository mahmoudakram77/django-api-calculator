from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.decorators import api_view
# Create your views here.

class HelloApi(APIView):
    def get(self,request):
        data ={
            'message':'hello django rest api'
        }
        return Response(data)

@api_view(["GET"])
def hello_drf(request):
    data={
        'message': 'hello django rest api . @api_view'
    }
    return Response(data)