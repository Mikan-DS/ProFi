from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def filter(request, filterName):
    return JsonResponse({'message': 'Not implemented'})


def filter_configs(request, filterName):
    print(filterName)
    return JsonResponse({'message': 'Not implemented'})
