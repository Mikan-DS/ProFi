from django.http import HttpResponse, JsonResponse

from ProOrientation.models import Employee, ContactData, Position


def index(request):
    return HttpResponse('<a href="/admin">Добавлять в админке, admin-admin</a>')


def add_mass_employees(request):
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
                print(name)
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