# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve as _serve


def serve(request, path):
    if '.' not in path:
        path = 'index.html'
    return _serve(request, path, '/vue')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('main.urls')),
    re_path(r'(?P<path>(^/?$|.*\.(js|css)))', serve)
]
