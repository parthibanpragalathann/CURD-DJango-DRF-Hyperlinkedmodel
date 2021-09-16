from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("athletics/category", views.AthleticsCategoriesView)
router.register("athletics", views.AthleticsView)
router.register("players", views.PlayersView)
router.register("competitions", views.CompetitionsView)

urlpatterns = [
    path("", include(router.urls))
]
