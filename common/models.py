from django.db import models


class AcademicYear(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField(verbose_name='Год')

    class Meta:
        verbose_name = 'Учебный год'
        verbose_name_plural = 'Учебные года'

    def __str__(self):
        return f"{self.year}-{self.year + 1}"


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'

    def __str__(self):
        return self.name


class Position(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.name


class InstitutionType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Вид учебного заведения'
        verbose_name_plural = 'Виды учебных заведений'

    def __str__(self):
        return self.name


class EventStatus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Название статуса')

    class Meta:
        verbose_name = 'Статус проведения'
        verbose_name_plural = 'Статусы проведения'

    def __str__(self):
        return self.name


class EventActivity(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Деятельность мероприятия'
        verbose_name_plural = 'Деятельности мероприятий'

    def __str__(self):
        return self.name


