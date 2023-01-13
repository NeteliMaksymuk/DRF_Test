from rest_framework import serializers
from .models import Tag, Events


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Events
        fields = '__all__'
