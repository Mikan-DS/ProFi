from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden

from ProOrientation.models import Employee, ContactData, Position, Event


def index(request):
    events = Event.objects.order_by('date')[:10]

    return render(request, "ProOrientation/index.html", {'events': events})

def events(request):
    events = Event.objects.all()

    return render(request, "ProOrientation/filter.html", {
        'events': events,
        'filter_object': "Мероприятия"
    })


def add_mass_employees(request):

    return HttpResponseForbidden("Этот путь закрыт!")

    qty = 0

    unknown = []

    if request.GET:
        values = request.GET.getlist('employees')[0]

        for pair in values.split("\n"):

            if not pair.strip():
                continue

            name, position = pair.split('\t')
            name = name.strip()
            last_name, first_name, middle_name = name.split(" ")

            if ContactData.objects.filter(last_name=last_name, first_name=first_name, middle_name=middle_name).first():
                continue
            position = Position.objects.filter(name=position.strip()).first()


            if position:

                cd = ContactData(first_name=first_name, last_name=last_name, middle_name=middle_name)


                cd.save()

                employee = Employee(contact=cd, specialty_id=7, position=position)

                employee.save()
                qty += 1

            else:
                unknown.append(pair)

    return JsonResponse({'added': qty, "unknown": unknown})