import uuid
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

from apps.authentication.models import User


# Create your models here.
class Research(models.Model):
    status_choices = (
        ("ongoing", "ongoing"),
        ("presented", "presented"),
        ("published", "published")
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    summary = models.TextField(max_length=1000)
    document = models.FileField(upload_to="research")
    created_on = models.DateField(auto_now_add=True)
    posted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="research_publisher")
    status = models.CharField(max_length=255, choices=status_choices)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return f"Research Title: {self.title}"

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
