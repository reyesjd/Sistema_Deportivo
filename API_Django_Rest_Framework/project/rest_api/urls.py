from django.urls import path
from rest_api.views import tablaPosiciones, detallesEquipo, historialPartidos, detallesPartido
urlpatterns = [
    path('tabla-posiciones/', tablaPosiciones),
    path('tabla-posiciones/<int:id>', detallesEquipo),
    path('historial-partidos/', historialPartidos),
    path('historial-partidos/<int:id>', detallesPartido)
]
