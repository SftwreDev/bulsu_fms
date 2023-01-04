import uuid
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django_ckeditor_5.fields import CKEditor5Field

from apps.authentication.models import User


class Announcements(models.Model):
    status = (
        ("draft", "draft"),
        ("published", "published"),
        ("closed", "closed")
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    content = CKEditor5Field(config_name='extends', null=True, blank=True)
    created_on = models.DateField(auto_now_add=True)
    posted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=255, choices=status)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return f"Announcement: {self.title}"


    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
