from django.urls import path
from .views import TagsView, EventsView, SingleEventView

urlpatterns = [
    path('tags/', TagsView.as_view(), name="all_tags"),
    path('events/', EventsView.as_view(), name="events"),
    path('event/<int:pk>/', SingleEventView.as_view(), name="single_events")
]
