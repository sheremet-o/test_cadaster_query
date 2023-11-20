from django.contrib import admin
from django.urls import path

from requests.views import history, ping, query, result

urlpatterns = [
    path("admin/", admin.site.urls),
    path('history', history, name='history'),
    path('ping', ping, name='ping'),
    path('query', query, name='query'),
    path('result', result, name='result'),
]
