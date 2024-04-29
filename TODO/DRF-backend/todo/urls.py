from django.urls import path
from . import views

urlpatterns = [
    path("", views.NoteList.as_view(), name="notes"),
    path("detail/<str:pk>/", views.NoteDetail.as_view(), name="note")
]
