from django.urls import path

from .views import *

app_name = "authentication"

urlpatterns = [
    path('signin', login_page, name="login"),
    path('signout', logout_view, name="logout"),
    path('signup', signup, name="signup"),
    path('email-verification-sent', email_verification_page, name="email_verification_page"),
    path('verify-email/<str:str>', verify_email, name="verify_email"),
    path('forgot-password', forgot_password, name="forgot_password"),
    path('reset-password/<str:str>', reset_password, name="reset_password"),
    path('user/delete/<str:id>', delete_user, name="delete_user"),

]