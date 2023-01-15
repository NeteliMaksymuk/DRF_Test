from django.contrib import admin
from .models import Tag, Events


class TagInstanceInline(admin.TabularInline):
    model = Tag


class EventsInstanceInline(admin.TabularInline):
    model = Events


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_name',)


@admin.register(Events)
class EventAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'category', 'created_at',)

