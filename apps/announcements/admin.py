from django.contrib import admin

# Register your models here.
from .models import *


class AnnouncementsAdmin(admin.ModelAdmin):
    list_display = ("title", "status",)
    prepopulated_fields = {"slug": ("title",)}  # new


admin.site.register(Announcements, AnnouncementsAdmin)
