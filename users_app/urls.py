from django.template.defaulttags import url
from django.urls import include, re_path, path
from rest_framework import routers
from form_app.views import FormViewSet, FormAppliersViewSet
from users_app.views import ActivateUser, AppliersViewSet, OwnerViewSet

router = routers.SimpleRouter()
router.register(r'auth/users/appliers', AppliersViewSet, basename='applier create')
router.register(r'auth/users/owners', OwnerViewSet, basename='applier create')
router.register(r'form_appliers', FormAppliersViewSet)
router.register(r'form', FormViewSet)
urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.jwt')),
    path('auth/users/activate/<uid>/<token>', ActivateUser.as_view({'get': 'activation'}), name='activation'),
]
