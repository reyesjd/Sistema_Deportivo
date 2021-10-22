import store from "../store"
import { get, post, remove, patch } from '@/services/http'
import { obtenerTodosEquipos } from '../services/equipos_services'

const obtenerTodosPartidos = async () => {
    const response = await get("historial-partidos/");
    const data = response.data
    if (data.success == true) {
        const partidos = data.partidos
        store.state.partidos = partidos
    }
};
const añadirPartido = async (data) => {

    const response = await post("historial-partidos/", data)
    obtenerTodosEquipos();
    obtenerTodosPartidos();
    alert(response.data.message)
}

const eliminarPartido = async (id) => {
    const response = await remove("historial-partidos/" + id)
    obtenerTodosPartidos();
    obtenerTodosEquipos();
    alert(response.data.message)
}

const editarPartido = async (data, id) => {
    console.log(id)
    const response = await patch("historial-partidos/" + id, data)
    obtenerTodosPartidos();
    obtenerTodosEquipos();
    alert(response.data.message)
}

export { obtenerTodosPartidos, añadirPartido, eliminarPartido, editarPartido }