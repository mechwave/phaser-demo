import { AxiosRequestConfig,  } from "axios";
import { axios, AxiosInstance, IAPIProvider } from "../types/index.d";
import { AxiosResponse } from 'axios';

class APIProvider implements IAPIProvider {
    options?: AxiosRequestConfig;
    _axios: AxiosInstance;
    constructor (options: any) {
        this.options = Object.assign({ basePath: '' }, options)
        this._axios = axios.create({
            headers: { 
                'Content-Type': 'application/json',
                // 'Authorization': {
                //   toString() {
                //       return `Bearer ${localStorage.getItem('token')}`
                //   }
                // } 
            }
        })
    }
    getUser() {
        return this._axios.get('/api/user/list').then((response: AxiosResponse) => {
            return response.data
        })
    }
}

export default new APIProvider({
})
