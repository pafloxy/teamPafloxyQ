from django.urls import path
from .views import GameListView

urlpatterns = [
    path("", GameListView.as_View(), name="home"),
]