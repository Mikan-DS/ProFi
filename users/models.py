import typing

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        """
        Creates and saves a User with the given username and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        """
        Creates and saves a superuser with the given username and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)


class User(AbstractUser):
    objects = UserManager()
    first_name = None
    last_name = None
    email = None
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'auth_user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class ContactData(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=255, blank=True, verbose_name='Отчество')
    phone = models.CharField(max_length=20, blank=True, verbose_name='Телефон')
    email = models.EmailField(blank=True, verbose_name='Почта')

    class Meta:
        verbose_name = 'Контактные данные'
        verbose_name_plural = 'Контактные данные'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    contact_data = models.ForeignKey('ContactData', on_delete=models.CASCADE, verbose_name='Контактные данные')
    department = models.ForeignKey('common.Department', on_delete=models.CASCADE, verbose_name='Подразделение')
    position = models.ForeignKey('common.Position', on_delete=models.CASCADE, verbose_name='Должность')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f"{self.contact_data}"


class School(models.Model):
    id = models.AutoField(primary_key=True)
    director = models.ForeignKey('ContactData', on_delete=models.CASCADE, verbose_name='Контактные данные директора')
    institution_type = models.ForeignKey(
        'common.InstitutionType',
        on_delete=models.CASCADE,
        verbose_name='Вид учебного заведения'
    )
    name = models.CharField(max_length=255, verbose_name='Название/номер школы')
    address = models.CharField(max_length=255, verbose_name='Адрес')

    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = 'Школы'

    def __str__(self):
        return self.name


class Partner(models.Model):
    id = models.AutoField(primary_key=True)
    contact_data = models.ForeignKey('ContactData', on_delete=models.CASCADE, verbose_name='Контактные данные партнера')
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание предприятия')

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'

    def __str__(self):
        return self.name


class Specialty(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='Название')
    number = models.CharField(max_length=255, verbose_name='Номер')
    head_contact_data = models.ForeignKey('ContactData', on_delete=models.CASCADE, verbose_name='Контактные данные руководителя')

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'

    def __str__(self):
        return self.name

class SchoolResponsibility(models.Model):
    id = models.AutoField(primary_key=True)
    academic_year = models.ForeignKey('common.AcademicYear', on_delete=models.CASCADE, verbose_name='Учебный год')
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, verbose_name='Ответственный')
    school = models.ForeignKey('School', on_delete=models.CASCADE, verbose_name='Школа')

    class Meta:
        verbose_name = 'Ответственный за школу'
        verbose_name_plural = 'Ответственные за школы'

    def __str__(self):
        return f"{self.employee} - {self.school} ({self.academic_year})"

class Group(models.Model):
    id = models.AutoField(primary_key=True)
    curator = models.ForeignKey('Employee', on_delete=models.CASCADE, verbose_name='ID сотрудника-куратора')
    specialty = models.ForeignKey('Specialty', on_delete=models.CASCADE, verbose_name='Специальность')
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.name

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    contact_data = models.ForeignKey('ContactData', on_delete=models.CASCADE, verbose_name='Контактные данные студента')
    group = models.ForeignKey('Group', on_delete=models.CASCADE, verbose_name='Группа')

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return f"{self.contact_data}"


