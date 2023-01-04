from django.contrib import admin

# Register your models here.
from .models import *


class ExtensionAdmin(admin.ModelAdmin):
    list_display = ("title",)
    prepopulated_fields = {"slug": ("title",)}  # new


admin.site.register(Extension, ExtensionAdmin)
