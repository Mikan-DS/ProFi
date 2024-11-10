from django.contrib import admin
from .models import *

# Определите классы администратора для каждой модели (необязательно, но рекомендуется)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'event_status', 'academic_year')

class EventOrganizerAdmin(admin.ModelAdmin):
    list_display = ('employee', 'event')

class EventDetailAdmin(admin.ModelAdmin):
    list_display = ('event_activity', 'event')

class EventParticipantAdmin(admin.ModelAdmin):
    list_display = ('student', 'event', 'participation_points')

class MethodicalFileAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'date_added', 'employee')

class RelevantMethodicalFileAdmin(admin.ModelAdmin):
    list_display = ('methodical_file', 'event_activity')

# Зарегистрируйте модели в admin.py
admin.site.register(Event, EventAdmin)
admin.site.register(EventOrganizer, EventOrganizerAdmin)
admin.site.register(EventDetail, EventDetailAdmin)
admin.site.register(EventParticipant, EventParticipantAdmin)
admin.site.register(MethodicalFile, MethodicalFileAdmin)
admin.site.register(RelevantMethodicalFile, RelevantMethodicalFileAdmin)