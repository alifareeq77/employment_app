from djoser.views import UserViewSet
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from form_app.views import IsStaff
from users_app.models import Appliers, Owner
from users_app.serializers import AppliersSerializer, OwnerSerializer


class ActivateUser(UserViewSet):
    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())

        # this line is the only change from the base implementation.
        kwargs['data'] = {"uid": self.kwargs['uid'], "token": self.kwargs['token']}
        print(kwargs)
        return serializer_class(*args, **kwargs)

    def activation(self, request, uid, token, *args, **kwargs):
        super().activation(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)


class AppliersViewSet(ModelViewSet):
    queryset = Appliers.objects.all()
    serializer_class = AppliersSerializer

    def get_queryset(self):
        user = self.request.user
        return Appliers.objects.filter(user=user)

class OwnerViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

    def get_queryset(self):
        user = self.request.user
        return Owner.objects.filter(user=user)
