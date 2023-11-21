from rest_framework import serializers
from users_app.models import CustomUser, Appliers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password']


class AppliersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appliers
        fields = ['user', 'first_name', 'last_name', 'email', 'password']
