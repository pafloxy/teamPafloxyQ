from django.views.generic import ListView
from .models import GamePost

# Create your views here.
class GameListView(ListView):
    model = GamePost
    template_name = "home.html"