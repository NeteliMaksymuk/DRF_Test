from django.contrib import admin

from .models import Tag, Events
# Register your models here.
admin.site.register(Tag)
admin.site.register(Events)