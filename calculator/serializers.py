from .models import *
from rest_framework import serializers


class NumericSerializer(serializers.ModelSerializer):
    class Meta():
        model = Numeric
        fields = ['numa', 'numb', 'result']