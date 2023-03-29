from django.urls import path

from .views import NoteListCreateAPIView, NoteDetailAPIView


urlpatterns = [
    path("notes/", NoteListCreateAPIView.as_view(), name="note-list"),
    path("notes/<int:pk>/", NoteDetailAPIView.as_view(), name="note-detail"),
]