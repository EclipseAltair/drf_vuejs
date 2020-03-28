# -*- coding: utf-8 -*-
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import CursorPagination
from .models import Car
from .serializers import CarSerializer


class MyPagination(CursorPagination):
    page_size = 15
    ordering = 'id'


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    pagination_class = MyPagination
    
    def filter_queryset(self, queryset):
        for k, v in self.request.query_params.items():
            if k == 'cursor':
                continue
            queryset = queryset.filter(**{k: v})
        return queryset

'''render on backend'''
# def all_cars(request):
#     result = []
#     cars = Car.objects.all()
#     for car in cars:
#         result.append(CarSerializer(car).data)
#     return JsonResponse(result, safe=False)
