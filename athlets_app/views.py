from rest_framework import viewsets
from .models import AthleticsCategories, Athletics, Players, Competitions
from .serializer import AthleticsCategorySerializer, AthleticsSerializer, PlayersSerializer, CompetitionsSerializer

# Create athletics views here.
class AthleticsCategoriesView(viewsets.ModelViewSet):
    queryset = AthleticsCategories.objects.order_by("name")
    serializer_class = AthleticsCategorySerializer

class AthleticsView(viewsets.ModelViewSet):
    queryset = Athletics.objects.order_by("name")
    serializer_class = AthleticsSerializer

class PlayersView(viewsets.ModelViewSet):
    queryset = Players.objects.order_by("name")
    serializer_class = PlayersSerializer

class CompetitionsView(viewsets.ModelViewSet):
    queryset = Competitions.objects.all()
    serializer_class = CompetitionsSerializer
