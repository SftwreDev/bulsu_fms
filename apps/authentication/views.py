from django.contrib import messages
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from apps.authentication.utils import *

from .forms import *
from .models import *


def login_page(request):
    template_name = "registration/signin.html"

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            check_email = User.objects.get(username=username)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                messages.error(request, "Invalid email address or password")

        except User.DoesNotExist:
            messages.error(request, "User doesn't exists. Please register.")
    return render(request, template_name)


def logout_view(request):
    logout(request)
    return redirect('authentication:login')


def signup(request):
    template_name = 'registration/staff_signup_form.html'
    form = ActorSignUpForm(request.POST or None, request.FILES or None)
    context = {
        "form": form
    }

    if request.method == "POST":
        profile_picture = request.FILES['profile_picture']
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email_address = request.POST.get('email_address')
        address = request.POST.get('address')
        birthday = request.POST.get('birthday')
        contact = request.POST.get('contact')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        account_type = request.POST.get('account_type')

        if password1 != password2:
            messages.error(request, "Password doesn't match")
        else:
            try:
                check_email = User.objects.get(email=email_address)
                messages.error(request, "Email address already exists")
            except User.DoesNotExist:
                if account_type == "faculty":
                    user = User.objects.create_user(
                        email=email_address,
                        password=password1,
                        first_name=first_name,
                        last_name=last_name,
                        username=username,
                        is_faculty=True,
                        is_verified=True,
                    )
                    Actor.objects.create(
                        address=address,
                        birthday=birthday,
                        contact=contact,
                        user_id=user.id,
                        profile_picture=profile_picture
                    )
                    return redirect("/signin")
                elif account_type == "department heads":
                    user = User.objects.create_user(
                        email=email_address,
                        password=password1,
                        first_name=first_name,
                        last_name=last_name,
                        username=username,
                        is_heads=True,
                        is_verified=True,
                    )
                    Actor.objects.create(
                        address=address,
                        birthday=birthday,
                        contact=contact,
                        user_id=user.id,
                        profile_picture=profile_picture
                    )
                    return redirect("/signin")
                elif account_type == "research coordinator":
                    user = User.objects.create_user(
                        email=email_address,
                        password=password1,
                        first_name=first_name,
                        last_name=last_name,
                        username=username,
                        is_res_coordinators=True,
                        is_verified=True,
                    )
                    Actor.objects.create(
                        address=address,
                        birthday=birthday,
                        contact=contact,
                        user_id=user.id,
                        profile_picture=profile_picture
                    )
                    return redirect("/signin")
                elif account_type == "extension coordinator":
                    user = User.objects.create_user(
                        email=email_address,
                        password=password1,
                        first_name=first_name,
                        last_name=last_name,
                        username=username,
                        is_ext_coordinators=True,
                        is_verified=True
                    )
                    Actor.objects.create(
                        address=address,
                        birthday=birthday,
                        contact=contact,
                        user_id=user.id,
                        profile_picture=profile_picture
                    )
                elif account_type == "admin":
                    user = User.objects.create_user(
                        email=email_address,
                        password=password1,
                        first_name=first_name,
                        last_name=last_name,
                        username=username,
                        is_verified=True,
                        is_staff=True,

                    )
                    Actor.objects.create(
                        address=address,
                        birthday=birthday,
                        contact=contact,
                        user_id=user.id,
                        profile_picture=profile_picture
                    )
                    return redirect("/signin")
    return render(request, template_name, context)

def change_password(request):
    template_name = "alert.html"
    if request.method == "POST":
        current_password = request.POST.get("currentPassword")
        new_password = request.POST.get("newPassword")
        confirm_password = request.POST.get("confirmPassword")
        user = authenticate(request, username=request.user.username, password=current_password)
        if user is not None:
            if new_password == confirm_password:
                user = User.objects.get(id=request.user.id)
                user.set_password(new_password)
                user.save()

                context = {
                    "status": "True",
                    "message": "Password changed successfully"
                }
                print(context)
                return render(request, template_name, context)
            else:
                context = {
                    "status": "False",
                    "message": "New password and confirm password doesn't match"
                }
                print(context)
                return render(request, template_name, context)
        else:
            context = {
                "status": "False",
                "message": "Wrong current password"
            }
            print(context)
            return render(request, template_name, context)

def delete_user(request, id):

    obj = User.objects.get(id=id)
    obj.delete()
    return redirect("/")
