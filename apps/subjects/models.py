import uuid
from django.db import models


# Create your models here.
class Subjects(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    course_code = models.CharField(max_length=255, unique=True)
    units = models.IntegerField()

    def __str__(self):
        return self.title
