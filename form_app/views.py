from rest_framework.permissions import BasePermission
from rest_framework.viewsets import ModelViewSet

from form_app.models import Form, FormAppliers
from form_app.srializers import FormSerializer


class IsStaff(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_staff


class FormViewSet(ModelViewSet):
    permission_classes = [IsStaff]
    queryset = Form.objects.all()
    serializer_class = FormSerializer

    def get_queryset(self):
        user = self.request.user
        return Form.objects.filter(user=user)


class FormAppliersViewSet(ModelViewSet):
    queryset = FormAppliers.objects.all()
    serializer_class = FormSerializer
    permission_classes = [IsStaff, ]
