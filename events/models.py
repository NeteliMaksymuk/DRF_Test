from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _


class Tag(models.Model):
    tag_name = models.CharField(max_length=128)


class Events(models.Model):
    class EventCategory(models.TextChoices):
        INFO = "In", _("Info")
        ATTENTION = "At", _("Attention")
        ALARM = "Al", _("Alarm")

    created_at = models.DateTimeField(default=datetime.now, null=True, blank=True, editable=False)
    user_id = models.IntegerField()
    event_type = models.TextField()  # ??
    descriptions = models.TextField()
    category = models.CharField(max_length=2, choices=EventCategory.choices, default=EventCategory.INFO)
    tagM2M = models.ForeignKey(Tag, on_delete=models.CASCADE)
