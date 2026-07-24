from django.urls import path

from . import views

urlpatterns = [
    path("create/", views.create, name="create"),
    path("read/", views.read, name="read"),
    path("delete/<int:id>/", views.delete, name="delete"),
    path("edit/<int:id>/", views.edit, name="edit")
]
