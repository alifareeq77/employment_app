from django.db import models


class Form(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    owner = models.ForeignKey('users_app.Owner', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    appliers = models.ManyToManyField('users_app.Appliers')


class FormAppliers(models.Model):
    class StatusChoices(models.TextChoices):
        PAID = 'PD', 'PAID'
        PENDING = 'P', 'PENDING'
        FAILED = 'F', 'FAILED'
    applier = models.ForeignKey('users_app.Appliers', on_delete=models.CASCADE)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    status = models.BooleanField()
