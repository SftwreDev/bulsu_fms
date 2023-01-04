from django.urls import path

from .views import *


urlpatterns = [
    path("announcements/<slug:slug>", announcements_detail, name="announcements_detail")
]
