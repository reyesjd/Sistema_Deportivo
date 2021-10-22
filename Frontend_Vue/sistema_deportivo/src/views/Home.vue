<template>
  <div class="home">
    <header>
      <h1>
        Sistema Deportivo
      </h1>
    </header>
    <div class="content">
      <div id="tabla">
        <h2>Tabla de Posiciones</h2>
        <table border="1">
          <thead>
            <th>Nombre</th>
            <th>PJ</th>
            <th>PG</th>
            <th>PP</th>
            <th>PE</th>
            <th>GF</th>
            <th>GC</th>
            <th>DF</th>
            <th>P</th>
          </thead>
          <tbody>
            <tr v-for="(equipo, index) in storedData.state.equipos" :key="index">
              <td>{{equipo.nombre}}</td>
              <td>{{equipo.partidos_jugados}}</td>
              <td>{{equipo.partidos_ganados}}</td>
              <td>{{equipo.partidos_perdidos}}</td>
              <td>{{equipo.partidos_empatados}}</td>
              <td>{{equipo.goles_a_favor}}</td>
              <td>{{equipo.goles_a_contra}}</td>
              <td>{{equipo.diferencia_goles}}</td>
              <td>{{equipo.puntos}}</td>
            </tr>
          </tbody>
        </table>
        <h4>Acciones:</h4>
        <div class="acciones">

          <div class="crear">
            <h5>Crear un Equipo:</h5>

            <form class="form" v-on:submit.prevent="addEquipo">
              <label for="name">Nombre de Equipo: </label>
              <input type="text" id="name" required v-model="nombreEquipo" />
              <input type="submit" value="Crear Equipo">
            </form>

          </div>
        </div>
      </div>
      <div id="partidos">
        <h2>Historial de Partidos</h2>
        <table border="1">
          <thead>
            <th>ID</th>
            <th>Local</th>
            <th>Visitante</th>
            <th>Goles Local</th>
            <th>Goles Visitante</th>
            <th>Fecha</th>
            <td>Acciones</td>
          </thead>
          <tbody v-if="storedData.state.datosCargados">
            <tr v-for="(partido, index) in storedData.state.partidos" :key="index">
              <td>{{partido.id_partido}}</td>
              <td>{{obtenerNombreEquipo(partido.equipo_local)}}</td>
              <td>{{obtenerNombreEquipo(partido.equipo_visitante)}}</td>
              <td>{{partido.goles_local}}</td>
              <td>{{partido.goles_visitante}}</td>
              <td>{{partido.fecha}}</td>
              <td><button v-on:click="eliminarPartido($event)" :value="partido.id_partido">Eliminar</button></td>
            </tr>
          </tbody>
          <tbody v-else>
            <tr v-for="(partido, index) in storedData.state.partidos" :key="index">
              <td>{{partido.id_partido}}</td>
              <td>{{partido.equipo_local}}</td>
              <td>{{partido.equipo_visitante}}</td>
              <td>{{partido.goles_local}}</td>
              <td>{{partido.goles_visitante}}</td>
              <td>{{partido.fecha}}</td>
              <td><button v-on:click="eliminarPartido($event)" :value="partido.id_partido">Eliminar</button></td>
            </tr>
          </tbody>

        </table>
        <h4>Acciones:</h4>
        <div class="acciones">

          <div class="crear">
            <h5>Editar un Partido:</h5>

            <form class="form" v-on:submit.prevent="editarPartido($event)">
              <label for="comboPartido">ID Partido: </label>
              <select id="comboPartido" required @change="seleccionarItem">
                <option v-for="(partido, index) in storedData.state.partidos" :key="index" :value="index">{{partido.id_partido}}</option>
              </select>
              <label v-if="storedData.state.datosCargados">Local: {{obtenerNombreEquipo(storedData.state.partidoSeleccionado.equipo_local)}}</label>
              <label v-if="storedData.state.datosCargados">Visitante: {{obtenerNombreEquipo(storedData.state.partidoSeleccionado.equipo_visitante)}}</label>
              <label for="goles_local">Goles Local: </label>
              <input type="number" id="goles_local" required v-model="editarGolesLocal" min=0 oninput="validity.valid||(value='');" />
              <label for="goles_visita">Goles Visita: </label>
              <input type="number" id="goles_visita" required v-model="editarGolesVisita" min=0 oninput="validity.valid||(value='');" />
              <label for="fecha">Fecha: </label>
              <input type="date" id="fecha" required v-model="editarFecha" />
              <input type="submit" value="Editar Partido">
            </form>

          </div>
          <div class="crear">
            <h5>Crear un Partido:</h5>

            <form class="form" v-on:submit.prevent="addPartido">
              <label for="comboLocal">Equipo Local: </label>
              <select id="comboLocal" required v-model="equipoLocal">
                <option v-for="(equipo, index) in storedData.state.equipos" :key="index" :value="index">{{equipo.nombre}}</option>
              </select>
              <label for="comboVisita">Equipo Visitante: </label>
              <select id="comboVisita" required v-model="equipoVisita">
                <option v-for="(equipo, index) in storedData.state.equipos" :key="index" :value="index">{{equipo.nombre}}</option>
              </select>
              <label for="goles_local">Goles Local: </label>
              <input type="number" id="goles_local" required v-model="golesLocal" min=0 oninput="validity.valid||(value='');" />
              <label for="goles_visita">Goles Visita: </label>
              <input type="number" id="goles_visita" required v-model="golesVisita" min=0 oninput="validity.valid||(value='');" />
              <label for="fecha">Fecha: </label>
              <input type="date" id="fecha" required v-model="fecha" />
              <input type="submit" value="Añadir Partido">
            </form>

          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { obtenerTodosPartidos,añadirPartido, eliminarPartido, editarPartido } from '@/services/partidos_services'
import { obtenerTodosEquipos, añadirEquipo } from '@/services/equipos_services'
import store from "../store"
export default {
  
  name: 'Home',
  components: {

  },
  data() {
    return{
      storedData: store,
      nombreEquipo: "",
      golesLocal: 0,
      golesVisita: 0,
      editarGolesLocal: 0,
      editarGolesVisita: 0,
      equipoLocal: 0,
      equipoVisita: 0,      
      fecha: new Date().toISOString(),
      editarFecha: new Date().toISOString(),
    };
  },
  beforeCreate: async () => {
    await obtenerTodosPartidos();
    await obtenerTodosEquipos();
    store.state.datosCargados = true;
    store.state.partidoSeleccionado = store.state.partidos[0]

  },
  mounted: () => {

  },
  methods: {
    obtenerNombreEquipo(id){
      const listaEquipo = store.state.equipos.filter(equipo => equipo.id_equipo == id)
      const equipo = listaEquipo[0]
      return equipo.nombre      
 

    },
    addEquipo(){
      const data = {
        "nombre": this.nombreEquipo,
        "partidos_jugados": 0,
        "partidos_ganados": 0,
        "partidos_perdidos": 0,
        "partidos_empatados": 0,
        "goles_a_favor": 0, 
        "goles_a_contra": 0,
        "puntos":0
      }
      añadirEquipo(data)
    },
    addPartido(){
      const data = {
        "equipo_visitante": store.state.equipos[this.equipoVisita].id_equipo,
        "equipo_local":  store.state.equipos[this.equipoLocal].id_equipo,
        "goles_visitante": this.golesVisita,
        "goles_local": this.golesLocal,
        "fecha": this.fecha+" 00:00:00"
      }
      añadirPartido(data)
    },
    eliminarPartido(e){
      const id = e.target.value;
      eliminarPartido(id)
      
    },
    editarPartido(){
      const id = store.state.partidoSeleccionado.id_partido;
      const data = {
        "equipo_visitante": store.state.equipos[store.state.partidoSeleccionado.equipo_visitante].id_equipo,
        "equipo_local":  store.state.equipos[store.state.partidoSeleccionado.equipo_local].id_equipo,
        "goles_visitante": this.editarGolesVisita,
        "goles_local": this.editarGolesLocal,
        "fecha": this.editarFecha+" 00:00:00"
      }
      editarPartido(data, id);
      
    },
    seleccionarItem(e){
      const id = e.target.value;
      store.state.partidoSeleccionado = store.state.partidos[id]
      console.log(store.state.partidoSeleccionado)
    }
  }

}
</script>
<style scoped>
.content {
  display: flex;
  justify-content: space-around;
}
.acciones {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 8px;
  padding: 16px;
  border: 2px solid gray;
}
.crear {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 12px;
  padding: 16px;
  border: 1px solid bisque;
}
#tabla {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
}
.form {
  display: flex;
  flex-direction: column;
  gap: 8px;
  align-items: flex-start;
}
#partidos {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
}
</style>
