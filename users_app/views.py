from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from djoser.views import UserViewSet
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from form_app.views import IsStaff
from users_app.forms import RegisterForm, LoginForm
from users_app.models import Appliers, CustomUser
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


# class AppliersViewSet(ModelViewSet):
#     queryset = Appliers.objects.all()
#     serializer_class = AppliersSerializer
#
#     def get_queryset(self):
#         user = self.request.user
#         return Appliers.objects.filter(user=user)
#
# class OwnerViewSet(ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = Owner.objects.all()
#     serializer_class = OwnerSerializer
#
#     def get_queryset(self):
#         user = self.request.user
#         return Owner.objects.filter(user=user)
'''
models view
'''


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = CustomUser.objects.create_user(form.cleaned_data['email'], form.cleaned_data['password1'])
            if user is not None:
                user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'])
                login(request=request, user=user)
                form.cleaned_data.pop('email')
                form.cleaned_data.pop('password1')
                form.cleaned_data.pop('password2')
                Appliers.objects.create(**form.cleaned_data, user=user)
                user.is_completed = True
                user.save()
                return redirect('pay_for_form')
    else:
        if not request.user.is_anonymous:
            return redirect('index')
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


# @user_passes_test(is_active)
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                if user.is_completed:
                    return redirect('index')
                else:
                    redirect('index')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


def not_staff(user):
    return not user.is_staff


@login_required
def index(request):
    return render(request, 'base.html')
