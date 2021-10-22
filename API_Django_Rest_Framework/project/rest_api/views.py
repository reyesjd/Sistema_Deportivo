from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_api.models import Equipo, Partido
from rest_api.serializers import SerializadorEquipo, SerializadorPartido

# ver la tabla de posiciones y agregar equipos a esta


@api_view(['GET', 'POST'])
def tablaPosiciones(request):
    if request.method == 'GET':
        equipos = Equipo.objects.all()
        equipos = equipos.order_by('-puntos', '-diferencia_goles')
        equipos_serializados = SerializadorEquipo(equipos, many=True)
        return Response({'success': True, 'equipos': equipos_serializados.data})

    elif request.method == 'POST':
        try:
            equipo_serializado = SerializadorEquipo(data=request.data)
            if equipo_serializado.is_valid():
                equipo_serializado.save()
                return Response({'success': True, 'message': 'Equipo añadido correctamente'})
            else:
                return Response({'success': False, 'message': 'Error: los datos enviados no corresponden con un equipo'})
        except:
            return Response({'success': False, 'message': 'Error: hubo un error al crear un equipo'}, )
    else:
        return Response({'success': False, 'message': "Error: no puede hacer una peticion "+request.method+" a esta ruta."})


# Ver detalles de un equipo en especifico a tarves de la ruta talabla-posiciones/id
@api_view(['GET', 'PATCH'])
def detallesEquipo(request, id):
    if request.method == 'GET':
        try:
            equipo = Equipo.objects.get(id_equipo=id)
            equipo_serializado = SerializadorEquipo(equipo)
            return Response({'success': True, 'equipos': equipo_serializado.data})
        except:
            return Response({'success': False, 'message': 'Error: no existe equipo con id='+str(id)}, )
    elif request.method == 'PATCH':
        try:
            equipo = Equipo.objects.get(id_equipo=id)
            equipo_serializado = SerializadorEquipo(
                equipo, data=request.data, partial=True)
            if equipo_serializado.is_valid():
                equipo_serializado.save()
                return Response({'success': True, 'message': 'Equipo actualizado correctamente'})
            else:
                return Response({'success': False, 'message': 'Error: los datos enviados no corresponden con un equipo'})
        except:
            return Response({'success': False, 'message': 'Error: hubo un error al actualizar el equipo'})
    else:
        return Response({'success': False, 'message': "Error: no puede hacer una peticion "+request.method+" a esta ruta."})


# Ver el historial de partidos
@api_view(['GET', 'POST'])
def historialPartidos(request):
    if request.method == 'GET':
        partidos = Partido.objects.all()
        partidos_serializados = SerializadorPartido(partidos, many=True)
        return Response({'success': True, 'partidos': partidos_serializados.data})

    elif request.method == 'POST':
        # try:
        if request.data['equipo_local'] != request.data['equipo_visitante']:
            partido_serializado = SerializadorPartido(data=request.data)
            if partido_serializado.is_valid():
                partido_serializado.save()
                id = int(partido_serializado.data['id_partido'])
                goles_local = int(partido_serializado.data['goles_local'])
                goles_visita = int(partido_serializado.data['goles_visitante'])
                añadirResultados(id, goles_local, goles_visita)
                return Response({'success': True, 'message': 'Partido añadido correctamente'})
            else:
                return Response({'success': False, 'message': 'Error: los datos enviados no corresponden con un partido'})
        else:
            return Response({'success': False, 'message': 'Error: No puede asignar un partido con el mismo equipo de local y visitante'}, )
        # except:
     #   return Response({'success': False, 'message': 'Error: hubo un error al crear el partido'}, )

    else:
        return Response({'success': False, 'message': "Error: no puede hacer una peticion "+request.method+" a esta ruta."})


# ver detalles de un partido y poder editarlo a traves de la ruta historial-partidos/id
@api_view(['GET', 'PATCH', 'DELETE'])
def detallesPartido(request, id):
    if request.method == 'GET':
        try:
            partido = Partido.objects.get(id_partido=id)
            partido_serializado = SerializadorPartido(partido)
            return Response({'success': True, 'equipos': partido_serializado.data})
        except:
            return Response({'success': False, 'message': 'Error: no existe partido con id='+str(id)})
    elif request.method == 'PATCH':
        try:
            partido = Partido.objects.get(id_partido=id)
            partido_serializado = SerializadorPartido(
                partido, data=request.data, partial=True)
            if partido_serializado.is_valid():
                partido_serializado.save()
                eliminarPartido(id)
                goles_local = int(partido_serializado.data['goles_local'])
                goles_visita = int(partido_serializado.data['goles_visitante'])
                añadirResultados(id, goles_local, goles_visita)
                return Response({'success': True, 'message': 'Partido actualizado correctamente'})
            else:
                return Response({'success': False, 'message': 'Error: los datos enviados no corresponden con un partido'})
        except:
            return Response({'success': False, 'message': 'Error: hubo un error al actualizar el partido con id'+str(id)})
    elif request.method == 'DELETE':
        try:
            eliminarPartido(id)
            partido = Partido.objects.get(id_partido=id)
            partido.delete()
            return Response({'success': True, 'message': 'Partido eliminado correctamente'})
        except:
            return Response({'success': False, 'message': 'Error: hubo un error al eliminar el partido con id'+str(id)}, )
    else:
        return Response({'success': False, 'message': "Error: no puede hacer una peticion "+request.method+" a esta ruta."})


def añadirResultados(pk, goles_local, goles_visitantes):

    partido = Partido.objects.get(id_partido=pk)
    visitante = partido.equipo_visitante
    local = partido.equipo_local

    local.partidos_jugados += 1
    visitante.partidos_jugados += 1

    local.goles_a_favor = local.goles_a_favor + goles_local
    visitante.goles_a_favor = visitante.goles_a_favor + goles_visitantes

    local.goles_a_contra = local.goles_a_contra + goles_visitantes
    visitante.goles_a_contra = visitante.goles_a_contra + goles_local

    local.diferencia_goles = local.goles_a_favor - local.goles_a_contra
    visitante.diferencia_goles = visitante.goles_a_favor - visitante.goles_a_contra

    if goles_local > goles_visitantes:
        local.partidos_ganados += 1
        visitante.partidos_perdidos += 1
        local.puntos += 1
    elif goles_visitantes > goles_local:
        visitante.partidos_ganados += 1
        local.partidos_perdidos += 1
        visitante.puntos += 3
    else:
        visitante.partidos_empatados += 1
        local.partidos_empatados += 1

    local.save()
    visitante.save()
    partido.save()


def eliminarPartido(pk):
    partido = Partido.objects.get(id_partido=pk)
    visitante = partido.equipo_visitante
    local = partido.equipo_local
    goles_local = partido.goles_local
    goles_visitantes = partido.goles_visitante

    local.partidos_jugados -= 1
    visitante.partidos_jugados -= 1

    local.goles_a_favor = local.goles_a_favor - goles_local
    visitante.goles_a_favor = visitante.goles_a_favor - goles_visitantes

    local.goles_a_contra = local.goles_a_contra - goles_visitantes
    visitante.goles_a_contra = visitante.goles_a_contra - goles_local

    local.diferencia_goles = local.goles_a_favor - local.goles_a_contra
    visitante.diferencia_goles = visitante.goles_a_favor - visitante.goles_a_contra

    if goles_local > goles_visitantes:
        local.partidos_ganados -= 1
        visitante.partidos_perdidos -= 1
        local.puntos -= 1
    elif goles_visitantes > goles_local:
        visitante.partidos_ganados -= 1
        local.partidos_perdidos -= 1
        visitante.puntos -= 3
    else:
        visitante.partidos_empatados -= 1
        local.partidos_empatados -= 1

    local.save()
    visitante.save()
