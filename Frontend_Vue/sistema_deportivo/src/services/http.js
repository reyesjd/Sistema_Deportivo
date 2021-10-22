import axios from 'axios';

const httpAPI = process.env.VUE_APP_RUTA_API

const get = async (endpoint) => {
    try {
        const url = `${httpAPI}/${endpoint}`;
        const config = {
            headers: {
                'Content-Type': 'application/json'
            }
        };
        const response = await axios.get(url, config);
        return response;
    } catch (err) {
        return null;
    }
};

const post = async (endpoint, data) => {
    try {
        const url = `${httpAPI}/${endpoint}`;
        const config = {
            headers: {
                'Content-Type': 'application/json'
            }
        };
        const response = await axios.post(url, data, config);
        return response;
    } catch (err) {
        console.log(err)
        return null;
    }
};

const patch = async (endpoint, data) => {
    try {
        const url = `${httpAPI}/${endpoint}`;
        const config = {
            headers: {
                'Content-Type': 'application/json',
            }
        };
        const response = await axios.patch(url, data, config);
        return response;
    } catch (err) {
        return null;
    }
};

const remove = async (endpoint) => {
    try {
        const url = `${httpAPI}/${endpoint}`;
        const config = {
            headers: {
                'Content-Type': 'application/json'
            }
        };
        const response = await axios.delete(url, config);
        return response;
    } catch (err) {
        return null;
    }
};

export { get, post, patch, remove };