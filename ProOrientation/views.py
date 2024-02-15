from django.http import HttpResponse

def index(request):
    return HttpResponse('<a href="/admin">Добавлять в админке, admin-admin</a>')
