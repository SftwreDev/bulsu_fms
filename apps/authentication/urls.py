from django.urls import path

from .views import *

app_name = "authentication"

urlpatterns = [
    path('signin', login_page, name="login"),
    path('signout', logout_view, name="logout"),
    path('signup', signup, name="signup"),
    path('update-password', change_password, name="change_password"),
    path('user/delete/<str:id>', delete_user, name="delete_user"),

]