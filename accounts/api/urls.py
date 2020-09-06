from django.urls import include, path
from .views import CustomRegisterView


urlpatterns = [
    path("", include("dj_rest_auth.urls")),
    path("register/", include("dj_rest_auth.registration.urls")),
]
