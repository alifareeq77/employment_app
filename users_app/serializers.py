from rest_framework import serializers
from users_app.models import CustomUser, Appliers, Owner


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password']


class AppliersSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())


    class Meta:
        model = Appliers
        fields = ['user', 'first_name', 'last_name', 'status']


class OwnerSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def create(self, validated_data):
        owner = Owner.objects.create(**validated_data)
        cu = CustomUser.objects.get(id=self.context['request'].user.id)
        cu.is_staff = True
        cu.save()
        return owner

    def get_queryset(self):
        if not self.context['request'].user.is_authenticated:
            return Owner.objects.none()  # Return an empty queryset if not authenticated

        return Owner.objects.filter(user=self.context['request'].user)

    class Meta:
        model = Owner
        fields = ['user', 'first_name', 'last_name', ]
