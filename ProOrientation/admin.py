from django.contrib import admin

from .models import *


admin.site.register(AcademicYear)
admin.site.register(EventStatus)
admin.site.register(Position)
admin.site.register(TypeOfEducationalInstitution)


admin.site.register(Partner)
admin.site.register(ContactData)

class SubdivisionsInline(admin.TabularInline):
    model = Employee
    extra = 1

class SubdivisionsAdmin(admin.ModelAdmin):
    inlines = (SubdivisionsInline,)

admin.site.register(Subdivision, SubdivisionsAdmin)

admin.site.register(Specialty)

admin.site.register(Employee)
admin.site.register(MethodologicalFile)



class SchoolResponsibleInline(admin.TabularInline):
    model = SchoolResponsible
    extra = 1

class SchoolAdmin(admin.ModelAdmin):
    inlines = (SchoolResponsibleInline,)

admin.site.register(School, SchoolAdmin)


admin.site.register(Student)

class EventOrganizerInline(admin.TabularInline):
    model = EventOrganizer
    extra = 1

class EventPlanInline(admin.TabularInline):
    model = EventDetails
    extra = 1

class EventParticipantInline(admin.TabularInline):
    model = EventParticipant
    extra = 1

class EventAdmin(admin.ModelAdmin):
    inlines = [
        EventOrganizerInline,
        EventPlanInline,
        EventParticipantInline,
    ]

admin.site.register(Event, EventAdmin)

class StudentInline(admin.TabularInline):
    model = Student
    extra = 1

class GroupAdmin(admin.ModelAdmin):
    inlines = [StudentInline]

admin.site.register(Group, GroupAdmin)
admin.site.register(EventDetails)
admin.site.register(EventActivity)
