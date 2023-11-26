from django.db import models


class Form(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    owner = models.ForeignKey('users_app.Owner', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FormAppliers(models.Model):
    class StatusChoices(models.TextChoices):
        PAID = 'PD', 'PAID'
        PENDING = 'P', 'PENDING'
        FAILED = 'F', 'FAILED'

    applier = models.ForeignKey('users_app.Appliers', on_delete=models.CASCADE)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=StatusChoices.choices)
    transaction = models.ForeignKey('form_app.TransactionHistory', null=True, on_delete=models.DO_NOTHING)


class TransactionHistory(models.Model):
    class SubscriptionChoices(models.IntegerChoices):
        THREE_MONTHS = 3, 'THREE MONTHS'
        SIX_MONTHS = 9, 'SIX MONTHS'

    user = models.ForeignKey('users_app.Appliers', on_delete=models.CASCADE)
    amount = models.IntegerField(choices=SubscriptionChoices.choices)
    transaction_id = models.CharField(max_length=256)
    def __str__(self):
        return self.transaction_id
