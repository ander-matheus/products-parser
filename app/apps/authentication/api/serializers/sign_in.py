from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class SignInSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    django_user = None

    def validate(self, attrs):
        check_user = User.objects.filter(username__iexact=attrs["username"]).first()

        if check_user and not check_user.is_active:
            if check_user.attempts >= settings.PASSWORD_ATTEMPTS:
                raise serializers.ValidationError(
                    _("Account blocked after {} attempts of login").format(
                        settings.PASSWORD_ATTEMPTS
                    )
                )
            else:
                raise serializers.ValidationError(_("Account inactive"))

        user = authenticate(username=attrs["username"], password=attrs["password"])
        if not user:
            raise serializers.ValidationError(_("Username and/or password invalid"))

        self.django_user = user
        return attrs
