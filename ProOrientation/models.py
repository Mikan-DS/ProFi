from django.contrib.auth.models import User
from django.db import models


class AcademicYear(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    year = models.IntegerField(verbose_name="Год", unique=True)

    class Meta:
        verbose_name = "Учебный год"
        verbose_name_plural = "Учебные годы"

    def __str__(self):
        return str(self.year) + "-" + str(self.year + 1)


class EventStatus(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=255, verbose_name="Название статуса", unique=True)

    class Meta:
        verbose_name = "Статус проведения"
        verbose_name_plural = "Статусы проведения"

    def __str__(self):
        return self.name


class EventActivity(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=255, verbose_name="Название", unique=True)

    class Meta:
        verbose_name = "Деятельность мероприятия"
        verbose_name_plural = "Деятельности мероприятий"

    def __str__(self):
        return self.name


class Position(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=255, verbose_name="Название", unique=True)

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"

    def __str__(self):
        return self.name


class TypeOfEducationalInstitution(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=255, verbose_name="Название", unique=True)

    class Meta:
        verbose_name = "Вид учебного заведения"
        verbose_name_plural = "Виды учебных заведений"

    def __str__(self):
        return self.name


class ContactData(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    last_name = models.CharField(max_length=255, verbose_name="Фамилия")
    middle_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Отчество")
    phone = models.CharField(max_length=255, blank=True, null=True, verbose_name="Телефон")
    email = models.EmailField(blank=True, null=True, verbose_name="Почта")

    class Meta:
        verbose_name = "Контактные данные"
        verbose_name_plural = "Контактные данные"

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name if self.middle_name else ''}".strip()


class Specialty(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    head = models.ForeignKey(ContactData, on_delete=models.CASCADE, verbose_name="Контактные данные руководителя")
    name = models.CharField(max_length=255, verbose_name="Название")
    number = models.CharField(max_length=255, verbose_name="Номер")

    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"

        unique_together = ("name", "number")

    def __str__(self):
        return self.name + ' (' + self.number + ')'


class School(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    director = models.ForeignKey(ContactData, on_delete=models.CASCADE, verbose_name="Контактные данные директора")
    type = models.ForeignKey(TypeOfEducationalInstitution, on_delete=models.CASCADE,
                             verbose_name="Вид учебного заведения")
    name = models.CharField(max_length=255, verbose_name="Название/номер школы")
    address = models.CharField(max_length=255, verbose_name="Адрес")

    class Meta:
        verbose_name = "Школа"
        verbose_name_plural = "Школы"

        unique_together = ("name", "address")

    def __str__(self):
        return f"{self.type.name} {self.name} ({self.address})"


class Partner(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    contact = models.ForeignKey(ContactData, on_delete=models.CASCADE, verbose_name="Контактные данные партнёра")
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание предприятия")

    class Meta:
        verbose_name = "Партнёр"
        verbose_name_plural = "Партнёры"

        unique_together = ("contact", "name")

    def __str__(self):
        return self.name


class Subdivision(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=255, verbose_name="Название", unique=True)

    class Meta:
        verbose_name = "Подразделение"
        verbose_name_plural = "Подразделения"

    def __str__(self):
        return self.name


class Employee(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    contact = models.OneToOneField(ContactData, on_delete=models.CASCADE, verbose_name="Контактные данные сотрудника")
    subdivision = models.ForeignKey(Subdivision, on_delete=models.SET_NULL, verbose_name="Подразделение", null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name="Должность")
    user = models.OneToOneField(User,
                                on_delete=models.SET_NULL,
                                verbose_name="Учетные данные",
                                null=True, blank=True,
                                related_name="employee")

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return f"пр. {self.contact}"


class SchoolResponsible(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Ответственный")
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, verbose_name="Учебный год")
    school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name="Школа")

    class Meta:
        verbose_name = "Ответственный за школу"
        verbose_name_plural = "Ответственные за школы"
        unique_together = ('employee', 'academic_year', 'school',)

    def __str__(self):
        return f"{self.employee.contact} - {self.school.name} ({self.academic_year})"


class Group(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    curator = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Куратор")
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, verbose_name="Специальность")
    name = models.CharField(max_length=255, verbose_name="Название", unique=True)

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def __str__(self):
        return self.name


class Student(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    contact = models.OneToOneField(ContactData,
                                on_delete=models.CASCADE,
                                verbose_name="Контактные данные студента")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Группа")

    user = models.OneToOneField(User,
                                on_delete=models.SET_NULL,
                                verbose_name="Учетные данные",
                                null=True, blank=True,
                                related_name="student")

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    def __str__(self):
        return f"студент {self.contact} ({self.group.name})"


class Event(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, verbose_name="Учебный год")
    status = models.ForeignKey(EventStatus, on_delete=models.CASCADE, verbose_name="Статус мероприятия")
    name = models.CharField(max_length=255, verbose_name="Название")
    location = models.CharField(max_length=255, verbose_name="Место проведения")
    date = models.DateTimeField(verbose_name="Дата проведения")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"

    def __str__(self):
        return self.name


class EventOrganizer(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Организатор")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name="Мероприятие")

    class Meta:
        verbose_name = "Организатор мероприятия"
        verbose_name_plural = "Организаторы мероприятий"
        unique_together = ('employee', 'event')


    def __str__(self):
        return str(self.id) + '-' + self.employee.contact.first_name + '-' + self.event.name


class EventPlan(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    event_activity = models.ForeignKey(EventActivity, on_delete=models.CASCADE,
                                       verbose_name="Вид деятельности мероприятия")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name="Мероприятие")

    class Meta:
        verbose_name = "План мероприятия"
        verbose_name_plural = "Планы мероприятий"
        unique_together = ('event_activity', 'event')


    def __str__(self):
        return str(self.id) + '-' + self.event_activity.name + '-' + self.event.name


class EventParticipant(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Студент")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name="Мероприятие")
    participation_score = models.IntegerField(verbose_name="Баллы за участие", default=0)

    class Meta:
        verbose_name = "Участник мероприятия"
        verbose_name_plural = "Участники мероприятий"
        unique_together = ('student', 'event')

    def __str__(self):
        return str(self.id) + '-' + self.student.contact.first_name + '-' + self.event.name


class MethodologicalFile(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, verbose_name="Специальность")
    name = models.CharField(max_length=255, verbose_name="Название")
    location = models.CharField(max_length=255, verbose_name="Расположение (ссылка)")
    date_added = models.DateTimeField(verbose_name="Дата добавления")

    class Meta:
        verbose_name = "Методический файл"
        verbose_name_plural = "Методические файлы"

    def __str__(self):
        return self.name


class RelevantMethodologicalFile(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    methodological_file = models.ForeignKey(MethodologicalFile, on_delete=models.CASCADE,
                                            verbose_name="Методический файл")
    event_activity = models.ForeignKey(EventActivity, on_delete=models.CASCADE, verbose_name="Вид деятельности")

    class Meta:
        verbose_name = "Релевантный методический файл"
        verbose_name_plural = "Релевантные методические файлы"
        unique_together = ("methodological_file", "event_activity")

    def __str__(self):
        return str(self.id) + '-' + self.methodological_file.name + '-' + self.event_activity.name

