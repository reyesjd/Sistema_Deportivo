import store from "../store"
import { get, post } from '@/services/http'

const obtenerTodosEquipos = async () => {
    const response = await get("tabla-posiciones/");
    const data = response.data

    if (data.success == true) {
        const equipos = data.equipos
        store.state.equipos = equipos
    }
};


const añadirEquipo = async (data) => {
    const response = await post("tabla-posiciones/", data)
    obtenerTodosEquipos();
    alert(response.data.message)
}

export { obtenerTodosEquipos, añadirEquipo }