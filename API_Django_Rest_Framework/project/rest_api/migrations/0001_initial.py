# Generated by Django 3.2.8 on 2021-10-22 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id_equipo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('partidos_jugados', models.IntegerField(default=0)),
                ('partidos_ganados', models.IntegerField(default=0)),
                ('partidos_perdidos', models.IntegerField(default=0)),
                ('partidos_empatados', models.IntegerField(default=0)),
                ('goles_a_favor', models.IntegerField(default=0)),
                ('goles_a_contra', models.IntegerField(default=0)),
                ('diferencia_goles', models.IntegerField(default=0)),
                ('puntos', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id_partido', models.AutoField(primary_key=True, serialize=False)),
                ('goles_visitante', models.IntegerField(default=0)),
                ('goles_local', models.IntegerField(default=0)),
                ('fecha', models.DateTimeField()),
                ('equipo_local', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='historial_local', to='rest_api.equipo')),
                ('equipo_visitante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='historial_visita', to='rest_api.equipo')),
            ],
        ),
    ]
