from django.template.defaulttags import url
from django.urls import include, re_path, path
from users_app import views
from rest_framework import routers
import form_app.views

# from form_app.views import FormViewSet, FormAppliersViewSet
# from users_app.views import ActivateUser, AppliersViewSet, OwnerViewSet
#
# router = routers.SimpleRouter()
# router.register(r'auth/users/appliers', AppliersViewSet, basename='applier create')
# router.register(r'auth/users/owners', OwnerViewSet, basename='applier create')
# router.register(r'form_appliers', FormAppliersViewSet)
# router.register(r'form', FormViewSet)
urlpatterns = [
    # path('', include(router.urls)),
    # re_path(r'^auth/', include('djoser.urls')),
    # re_path(r'^auth/', include('djoser.urls.jwt')),
    # path('auth/users/activate/<uid>/<token>', ActivateUser.as_view({'get': 'activation'}), name='activation'),
    path('user/signup', views.register, name='signup'),
    path('user/login', views.login_view, name='login'),
    path('user/logout', views.logout_view, name='logout'),
    path('', views.index, name='index')
]
