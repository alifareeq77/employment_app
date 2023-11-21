from django.template.defaulttags import url
from django.urls import include, re_path, path

from users_app.views import ActivateUser

urlpatterns = [
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.jwt')),
    path('auth/users/activate/<uid>/<token>', ActivateUser.as_view({'get': 'activation'}), name='activation')
]
