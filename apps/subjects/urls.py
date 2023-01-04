from django.urls import path


from .views import *


urlpatterns = [
    path("subjects/add", faculty_add_subjs, name="faculty_add_subjs"),
    path("subjects/remove/<str:id>", remove_faculty_subjs, name="remove_faculty_subjs")
]