import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.subjects.models import Subjects


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_faculty = models.BooleanField(default=False)
    is_res_coordinators = models.BooleanField(default=False)
    is_ext_coordinators = models.BooleanField(default=False)
    is_heads = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Actor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="user_actor")
    profile_picture = models.ImageField(upload_to="profile_picture")
    address = models.CharField(max_length=255)
    birthday = models.DateField(auto_now_add=False)
    contact = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    position = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.first_name} | {self.user.last_name}"


class Faculty(Actor):
    subjects = models.ManyToManyField(Subjects, related_name="faculty_subjects")

    def __str__(self):
        return self.user.last_name + self.user.first_name


class Departments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    department = models.CharField(max_length=255, unique=True)
    headed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="dept_headed_by")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="dept_created_by")

    def __str__(self):
        return self.department
