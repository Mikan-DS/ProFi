from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addmassemployees/', views.add_mass_employees, name='add_mass_employees')
]
