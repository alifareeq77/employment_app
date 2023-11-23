from rest_framework import serializers

from form_app.models import Form, FormAppliers
from users_app.models import Appliers


class FormSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    appliers = serializers.PrimaryKeyRelatedField(many=False, queryset=Appliers.objects.all())

    class Meta:
        model = Form
        fields = ['name', 'description', 'owner', 'password', 'appliers']
        extra_kwargs = {"appliers": {"required": False, "allow_null": True}}


class FormAppliersSerializers(serializers.ModelSerializer):
    status = serializers.HiddenField(default=FormAppliers.StatusChoices.PENDING)

    class Meta:

        model = FormAppliers
        fields = ['applier', 'form', 'status']
