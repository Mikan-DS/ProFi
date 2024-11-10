from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.admin_forms import UserCreationForm, UserChangeForm
from users.models import User, ContactData, Employee, School, Partner, Specialty, SchoolResponsibility, Group, Student


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ("username", "is_staff",)
    list_filter = ("username", "is_staff",)
    fieldsets = (
        (None, {"fields": ("username", "password",)}),
        ("Разрешения", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "password1", "password2", "is_staff"
            )}
         ),
    )
    search_fields = ("username", )
    ordering = ("id",)


admin.site.register(User, CustomUserAdmin)


@admin.register(ContactData)
class ContactDataAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'middle_name', 'phone', 'email')
    search_fields = ('first_name', 'last_name', 'middle_name', 'phone', 'email')


# Определите классы администратора для каждой модели (необязательно, но рекомендуется)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('contact_data', 'department', 'position')



class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'director', 'institution_type')

class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_data')

class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'head_contact_data')

class SchoolResponsibilityAdmin(admin.ModelAdmin):
    list_display = ('academic_year', 'employee', 'school')

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'curator', 'specialty')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('contact_data', 'group')


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Specialty, SpecialtyAdmin)
admin.site.register(SchoolResponsibility, SchoolResponsibilityAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Student, StudentAdmin)
