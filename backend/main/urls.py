# -*- coding: utf-8 -*-
from rest_framework.routers import DefaultRouter
from main.views import CarViewSet

router = DefaultRouter()
router.register('cars', CarViewSet)

urlpatterns = router.urls
