from django.urls import path

from . import views #dentro de esta ruta ( . ) importame las views.

urlpatterns = [
    path("test", views.index, name="index"),
]