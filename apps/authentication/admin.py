from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(User)
admin.site.register(Actor)
admin.site.register(Faculty)
admin.site.register(Departments)