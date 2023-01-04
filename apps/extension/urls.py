from django.urls import path

from .views import *


urlpatterns = [
    path("extension/<slug:slug>", extension_detail, name="extension_detail"),
    path("extension/delete/<slug:slug>", extension_delete, name="extension_delete"),
    path("extension/filter", filter_extension, name="filter_extension"),
]
