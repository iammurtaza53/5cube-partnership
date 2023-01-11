const axios = require("axios");


const instance = axios.create({
    baseURL: 'http://localhost:8000',
    timeout: 3000 * 180,
    Headers: {
        'Content-Type': 'application/json'
    }
});


export default {

    post(url, data) {
        return instance
            .post(url, data)
            .then((response) => {
                response.data["status"] = 200;
                return response.data;
            })
            .catch((err) => {
                return err;
            });
    },

    get(url) {
        return instance
            .get(url)
            .then((response) => {
                return response.data;
            })
            .catch((err) => {
                console.log(err.message);
                return err;
            });
    },

    delete(url,data) {
        
        return instance
            .delete(url,data)
            .then((response) => {
                return response.data;
            })
            .catch((err) => {
                return err;
            });
    },

    patch(url, data) {
        return instance
            .patch(url, data)
            .then((response) => {
                return response.data;
            })
            .catch((err) => {
                console.log(err.response.data);
                return err;
            });
    },

    put(url, data) {
        return instance
            .put(url, data)
            .then((response) => {
                return response.data;
            })
            .catch((err) => {
                console.log("err==>",err.response.data);
                return err;
            });
    },
};
