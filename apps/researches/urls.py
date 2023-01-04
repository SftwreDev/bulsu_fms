from django.urls import path


from .views import *


urlpatterns = [
    path("research/add", add_research, name="add_research"),
    path("research/delete/<str:id>", delete_research, name="delete_research"),
    path("research/filter", filter_research, name="filter_research"),
]