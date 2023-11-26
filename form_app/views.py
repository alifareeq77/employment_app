from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, redirect
from rest_framework.permissions import BasePermission
from rest_framework.viewsets import ModelViewSet

from form_app.forms import FormForm, PaymentOptionForm
from form_app.models import Form, FormAppliers, TransactionHistory
from form_app.payment_zain import pay, transaction_analysis
from form_app.srializers import FormSerializer
from users_app.models import Owner, Appliers


def _is_completed(user):
    return user.is_completed


def is_staff(user):
    return user.is_staff


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


@user_passes_test(_is_completed, is_staff)
def payment_test(request):
    if request.method == 'POST':
        return redirect(pay(1, 3))
    forms = Form.objects.all()
    return render(request, 'form_app/payment.html', {
        "forms": forms,
    })


@login_required
def pay_for_form(request,form_id):
    if request.method == 'POST':
        form = PaymentOptionForm(request.POST)
        if form.is_valid():
            # Process the selected payment plan
            selected_plan = form.cleaned_data['plan']
            return redirect(pay(service=int(selected_plan), form_id=form_id, ))
    return render(request, 'pay_for_form.html')


@login_required
def transaction(request):
    token = request.GET.get('token')
    print(token)
    result = transaction_analysis(token)
    print(result)
    status = result['status']
    if result['status'] == 'success':
        TransactionHistory.objects.create(user=Appliers.objects.filter(user=request.user)[0],
                                          transaction_id=result['id'], amount=result['amount'])

    return render(request, 'transaction_detail.html', {"result": result})


@login_required
@user_passes_test(is_staff)
def form_create(request):
    if request.method == 'POST':
        form = FormForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.owner = Owner.objects.filter(user=request.user)[0]
            form.save()
            return redirect('form_list')

    else:
        form = FormForm()

    return render(request, 'form_create.html', {'form': form})


@login_required
@user_passes_test(is_staff)
def form_list(request):
    forms = Form.objects.all().filter(owner=Owner.objects.filter(user=request.user)[0])
    return render(request, 'form_list.html', {'forms': forms})


@login_required
@user_passes_test(is_staff)
def form_detail(request, pk):
    try:
        form = Form.objects.get(pk=pk, owner=Owner.objects.get(user=request.user))
        form_appliers = FormAppliers.objects.filter(form=form)
        return render(request, 'form_detail.html', {'form': form, 'form_appliers': form_appliers})
    except Form.DoesNotExist:
        return redirect('form_list')


@login_required
@user_passes_test(is_staff)
def delete_form_applier(request, form_pk, applier_pk):
    form_applier = FormAppliers.objects.get(form_id=form_pk, applier_id=applier_pk)
    form_applier.delete()

    return redirect('form_detail', form_pk)
