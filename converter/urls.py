from django.urls import path
from . import views


urlpatterns = [path("", views.FileFieldView.as_view(), name="index")]
