from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.admin_forms import UserCreationForm, UserChangeForm
from users.models import User, ContactData


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