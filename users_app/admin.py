from django.contrib import admin

from form_app.models import FormAppliers, TransactionHistory
from users_app.models import CustomUser, Owner, Appliers


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    pass


@admin.register(Appliers)
class AppliersAdmin(admin.ModelAdmin):
    pass


@admin.register(FormAppliers)
class FormAppliersAdmin(admin.ModelAdmin):
    pass


@admin.register(TransactionHistory)
class TransactionHistoryAdmin(admin.ModelAdmin):
    pass
