from rest_framework.views import APIView
from .serializers import Tag, EventSerializer
from rest_framework.response import Response


class TagsView(APIView):
    def get(self):
        tags = [tag.tag_name for tag in Tag.objects.all()]
        return Response(tags)


class EventsView(APIView):
    def get(self):
        # Получить список всех событий за период.
        # Во входящих фильтрах: от(iso datetime string), до(iso datetime string),
        # типы событий(один/несколько, опционально). Возвращает все поля, включая
        # список тегов, кроме текстового описания.
        pass


class SingleEventView(APIView):
    def get(self):
        # Получить детальное описание события
        # - все атрибуты модели, включая м2м
        pass
    def put(self):
        # Редактирование события
        pass
    def post(self):
        # Создание нового события,
        # включая теги м2м из текстовой строки
        # через точку с запятой
        pass
    def delete(self):
        # Удаление события, если его статус не равен тревоги.
        # В противном случае ошибка доступа
        pass