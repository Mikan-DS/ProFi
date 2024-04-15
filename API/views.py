from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from API.filters import Filter

def api_response(message='Ok', code=200, **data):
    return JsonResponse({'message': message, **data}, status=code)

@csrf_exempt
def filter(request, filterName):
    return api_response("Not implemented", 405)

@csrf_exempt
def filter_configs(request, filterName):
    filter_object = Filter.get_filter(filterName)

    if not filter_object:
        return api_response("Filter does not exist", 404)

    return JsonResponse({'message': 'Filter found', "configs": filter_object.json})
