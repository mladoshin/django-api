from django.db import models
import uuid
# Create your models here.

class User(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4())
    activity = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=30, default="")