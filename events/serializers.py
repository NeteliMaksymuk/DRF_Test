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
        read_only_fields = ('user_id',)



class EventWithoutDescriptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Events
        fields = ['created_at', 'user_id', 'event_type', 'category', 'tagM2M' ]