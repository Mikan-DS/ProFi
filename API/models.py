from django.db import models

from django.db import models
from common.models import AcademicYear, Department, Position, InstitutionType, EventStatus, EventActivity

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    academic_year = models.ForeignKey(
        AcademicYear,
        on_delete=models.CASCADE,
        verbose_name='Учебный год',
        related_name='events'
    )
    event_status = models.ForeignKey(EventStatus, on_delete=models.CASCADE, verbose_name='Статус мероприятия')
    name = models.CharField(max_length=255, verbose_name='Название')
    location = models.CharField(max_length=255, verbose_name='Место проведения')
    date = models.DateField(verbose_name='Дата проведения')
    description = models.TextField(blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return self.name

class EventOrganizer(models.Model):
    id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(
        'users.Employee',
        on_delete=models.CASCADE,
        verbose_name='ID сотрудника-организатора',
        related_name='organizers'
    )
    event = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name='ID мероприятия')

    class Meta:
        verbose_name = 'Организатор мероприятия'
        verbose_name_plural = 'Организаторы мероприятий'

    def __str__(self):
        return f"{self.employee} - {self.event}"

class EventDetail(models.Model):
    id = models.AutoField(primary_key=True)
    event_activity = models.ForeignKey(EventActivity, on_delete=models.CASCADE, verbose_name='ID вида деятельности мероприятия')
    event = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name='ID мероприятия')

    class Meta:
        verbose_name = 'Деталь мероприятия'
        verbose_name_plural = 'Детали мероприятий'

    def __str__(self):
        return f"{self.event_activity} - {self.event}"

class EventParticipant(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(
        'users.Student',
        on_delete=models.CASCADE, verbose_name='ID студента',
        related_name='participants'
    )
    event = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name='ID мероприятия')
    participation_points = models.IntegerField(verbose_name='Баллы за участие')

    class Meta:
        verbose_name = 'Участник мероприятия'
        verbose_name_plural = 'Участники мероприятий'

    def __str__(self):
        return f"{self.student} - {self.event}"

class MethodicalFile(models.Model):
    id = models.AutoField(primary_key=True)
    specialty = models.ForeignKey(
        'users.Specialty',
        on_delete=models.CASCADE,
        verbose_name='Специальность',
        related_name='methodical_files'
    )
    name = models.CharField(max_length=255, verbose_name='Название')
    location = models.FileField(verbose_name='Файл', upload_to='methodical_files')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    employee = models.ForeignKey(
        'users.Employee',
        on_delete=models.CASCADE,
        verbose_name='ID сотрудника',
        related_name='methodical_files'
    )

    class Meta:
        verbose_name = 'Методический файл'
        verbose_name_plural = 'Методические файлы'

    def __str__(self):
        return self.name

class RelevantMethodicalFile(models.Model):
    id = models.AutoField(primary_key=True)
    methodical_file = models.ForeignKey('MethodicalFile', on_delete=models.CASCADE, verbose_name='ID методического файла')
    event_activity = models.ForeignKey(EventActivity, on_delete=models.CASCADE, verbose_name='ID вида деятельности')

    class Meta:
        verbose_name = 'Релевантный методический файл'
        verbose_name_plural = 'Релевантные методические файлы'

    def __str__(self):
        return f"{self.methodical_file} - {self.event_activity}"
