from django.urls import path

from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("department/delete/<str:id>", delete_department, name="delete_department"),
]