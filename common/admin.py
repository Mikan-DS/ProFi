from django.contrib import admin

from common.models import AcademicYear, Department, Position, InstitutionType, EventStatus, EventActivity

class AcademicYearAdmin(admin.ModelAdmin):
    list_display = ('year',)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)

class PositionAdmin(admin.ModelAdmin):
    list_display = ('name',)

class InstitutionTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

class EventStatusAdmin(admin.ModelAdmin):
    list_display = ('name',)

class EventActivityAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Зарегистрируйте модели в admin.py
admin.site.register(AcademicYear, AcademicYearAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Position, PositionAdmin)

admin.site.register(InstitutionType, InstitutionTypeAdmin)
admin.site.register(EventStatus, EventStatusAdmin)
admin.site.register(EventActivity, EventActivityAdmin)