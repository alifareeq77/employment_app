from django.urls import path

from form_app import views
from form_app.views import form_detail

urlpatterns = [
    # path('payment_test', views.payment_test, name='pay'),
    path('forms/create/', views.form_create, name='form_create'),
    path('forms/', views.form_list, name='form_list'),
    path('transaction', views.transaction, name='transaction'),
    path('payforform', views.pay_for_form, name='pay_for_form'),
    path('forms/<int:pk>/', form_detail, name='form_detail'),
    path('forms/<int:form_pk>/delete-applier/<int:applier_pk>/', views.delete_form_applier, name='delete_form_applier'),
]
