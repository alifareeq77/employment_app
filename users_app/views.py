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
from users_app.forms import RegisterForm, LoginForm, ApplierForm, OwnerForm
from users_app.models import Appliers, Owner, CustomUser
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
        print(form.is_valid())
        if form.is_valid():
            user = CustomUser.objects.create_user(form.cleaned_data['email'], form.cleaned_data['password1'])
            if user is not None:
                user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'])
                login(request=request, user=user)
                if form.cleaned_data["type"] == 'applier':
                    return redirect('applier_create')
                elif form.cleaned_data["type"] == 'owner':
                    return redirect('owner_create')
                else:
                    return HttpResponse("dont play with the form :)")
    else:
        if not request.user.is_anonymous:
            return redirect('test')
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
                print('logged in ')
                if user.is_completed:
                    return redirect('test')
                else:
                    redirect('applier_create')
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
@user_passes_test(not_staff)
def applier_create(request):
    if request.user.is_completed == False:
        if request.method == 'POST':
            form = ApplierForm(request.POST)
            if form.is_valid():
                applier = form.save(commit=False)
                user = CustomUser.objects.filter(email=request.user.email)[0]
                applier.user = user
                applier.save()
                user.is_completed = True
                user.save()
                return redirect('pay')

        else:
            form = ApplierForm()

        return render(request, 'applier_create.html', {'form': form})
    else:
        return redirect('pay')


@login_required
def owner_create(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)

        if form.is_valid():
            owner = form.save(commit=False)
            owner.user = request.user
            request.user.is_staff = True
            request.user.is_completed = True
            owner.save()
            request.user.save()
            return redirect('form_create')

    else:
        form = OwnerForm()

    return render(request, 'owner_create.html', {'form': form})


def auth_test(request):
    return render(request, 'auth_test.html')
