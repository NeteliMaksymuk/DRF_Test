from datetime import datetime
import base64
import json
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.backends import TokenBackend
from django.shortcuts import get_object_or_404
from rest_framework import status,permissions
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .serializers import Tag, EventSerializer, EventWithoutDescriptionsSerializer
from rest_framework.response import Response
from .add_tags import tags_text_to_db
from .models import Events
class TagsView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        tags = [tag.tag_name for tag in Tag.objects.all()]
        return Response(tags)


class EventsView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        # Получить список всех событий за период.
        # Во входящих фильтрах: от(iso datetime string), до(iso datetime string),
        # типы событий(один/несколько, опционально). Возвращает все поля, включая
        # список тегов, кроме текстового описания.

        iso_datetime_string_begin = request.data['iso_datetime_string_begin']
        iso_datetime_string_end = request.data['iso_datetime_string_end']
        events = Events.objects.filter(created_at__range=[iso_datetime_string_begin,
                                                         iso_datetime_string_end])
        serializer = EventWithoutDescriptionsSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Создание нового события,
        # включая теги м2м из текстовой строки
        # через точку с запятой

        request.data['user_id'] = request.user.id
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            tags_text_to_db(request.data.get('tagM2M'))

        return Response(serializer.data)  # ??


class SingleEventView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, pk):
        # Получить детальное описание события
        # - все атрибуты модели, включая м2м

        # НЕ гарно видaє поправити!!!!
        events = Events.objects.filter(id=pk)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        # Редактирование события

        instance = get_object_or_404(Events.objects.all(), pk=pk)
        serializer = EventSerializer(instance, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


    def delete(self, request, pk):
        # Удаление события, если его статус не равен тревоги.
        # В противном случае ошибка доступа

        events = Events.objects.filter(id=pk)
        serializer = EventSerializer(events, many=True)
        if serializer.data[0]['category'] != 'At':
            events.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(402) # FIX