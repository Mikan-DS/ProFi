from django.urls import path
from . import views

urlpatterns = [
    path('filter/<str:filterName>', views.filter, name='filter'),
    path('get/filter/<str:filterName>', views.filter_configs, name='filterConfigs'),
]
