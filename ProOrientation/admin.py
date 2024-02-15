from django.contrib import admin

from .models import *


admin.site.register(AcademicYear)
admin.site.register(EventStatus)
admin.site.register(Position)
admin.site.register(TypeOfEducationalInstitution)


admin.site.register(Partner)
admin.site.register(ContactData)
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
    model = EventPlan
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
