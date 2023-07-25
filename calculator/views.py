from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import NumericSerializer
from .models import Numeric

class CalculatorView(viewsets.ModelViewSet):
    queryset = Numeric.objects.all()
    serializer_class = NumericSerializer

    @action(methods=["POST"], detail=False)
    def add(self, request):
        serializer = NumericSerializer(data=request.data)
        if serializer.is_valid():
            numeric = serializer.validated_data
            numeric['result'] = numeric['numa'] + numeric['numb']
            return Response(numeric)
        else:
            return Response({'status': 'error', 'message': 'invalid request'})

    @action(methods=["POST"], detail=False)
    def subtract(self, request):
        serializer = NumericSerializer(data=request.data)
        if serializer.is_valid():
            numeric = serializer.validated_data
            numeric['result'] = numeric['numa'] - numeric['numb']
            return Response(numeric)
        else:
            return Response({'status': 'error', 'message': 'invalid request'})

    @action(methods=["POST"], detail=False)
    def multiply(self, request):
        serializer = NumericSerializer(data=request.data)
        if serializer.is_valid():
            numeric = serializer.validated_data
            numeric['result'] = numeric['numa'] * numeric['numb']
            return Response(numeric)
        else:
            return Response({'status': 'error', 'message': 'invalid request'})

    @action(methods=["POST"], detail=False)
    def division(self, request):
        serializer = NumericSerializer(data=request.data)
        if serializer.is_valid():
            numeric = serializer.validated_data
            numeric['result'] = numeric['numa'] / numeric['numb']
            return Response(numeric)
        else:
            return Response({'status': 'error', 'message': 'invalid data'})
