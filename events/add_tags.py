from .serializers import TagSerializer


def tags_text_to_db(tags):
    list_tags = tags.split(';')
    for i in range(len(list_tags)):
        if list_tags[i] != '':
            serializer = TagSerializer(data={'tag_name': list_tags[i]})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
