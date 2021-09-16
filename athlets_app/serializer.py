from rest_framework import serializers
from .models import AthleticsCategories, Athletics, Players, Competitions

class AthleticsCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AthleticsCategories
        fields = ("id", "url", "name")

class AthleticsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Athletics
        fields = ("id", "url", "name", "athletics_category", "join_date", "is_participated", "created_at")

class PlayersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Players
        fields = ("id", "url", "name", "gender", "number_race", "created_at")

class CompetitionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Competitions
        fields = ("id", "url", "athletics", "players", "distance", "date")
