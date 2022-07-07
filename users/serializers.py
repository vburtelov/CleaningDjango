from rest_framework import serializers

from users.models import CustomUser, CustomGroup


class CustomGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomGroup
        exclude = ('permissions',)


class CustomUserSerializer(serializers.ModelSerializer):
    groups = CustomGroupSerializer(many=True)

    class Meta:
        model = CustomUser
        exclude = ('password',)
