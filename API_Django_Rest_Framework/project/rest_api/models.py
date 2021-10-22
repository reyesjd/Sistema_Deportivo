from django.db import models


class Equipo(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    partidos_jugados = models.IntegerField(default=0)
    partidos_ganados = models.IntegerField(default=0)
    partidos_perdidos = models.IntegerField(default=0)
    partidos_empatados = models.IntegerField(default=0)
    goles_a_favor = models.IntegerField(default=0)
    goles_a_contra = models.IntegerField(default=0)
    diferencia_goles = models.IntegerField(default=0)
    puntos = models.IntegerField(default=0)


"""
{
"nombre": "Colombia",
"partidos_jugados": 0,
"partidos_ganados": 0,
"partidos_perdidos": 0,
"partidos_empatados": 0,
"goles_a_favor": 0, 
"goles_a_contra": 0
}
"""


class Partido(models.Model):
    id_partido = models.AutoField(primary_key=True)
    equipo_visitante = models.ForeignKey(
        Equipo, on_delete=models.PROTECT, related_name="historial_visita")
    equipo_local = models.ForeignKey(
        Equipo, on_delete=models.PROTECT, related_name="historial_local")
    goles_visitante = models.IntegerField(default=0)
    goles_local = models.IntegerField(default=0)
    fecha = models.DateTimeField(null=True)


"""
{
"id_partido": 1,
"equipo_visitante": 1,
"equipo_local": 1,
"goles_visitante": 2,
"goles_local": 3,
"fecha": "2021-10-19 00:00:00"
}
"""
