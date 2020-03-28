# -*- coding: utf-8 -*-
from rest_framework.serializers import ModelSerializer
from main.models import Car


class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
