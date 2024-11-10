from django.contrib.auth.forms import (
    UserCreationForm as DefaultUserCreationForm,
    UserChangeForm as DefaultUserChangeForm
)

from users.models import User


class UserCreationForm(DefaultUserCreationForm):
    class Meta:
        model = User
        fields = ()


class UserChangeForm(DefaultUserChangeForm):
    class Meta:
        model = User
        fields = ()
