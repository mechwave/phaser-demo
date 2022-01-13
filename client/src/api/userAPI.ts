// import axios from 'axios'
// const axiosInstance = axios.create({
//     // headers: { 
//     //     'Content-Type': 'application/json',
//     //     'Authorization': {
//     //       toString() {
//     //           return `Bearer ${localStorage.getItem('token')}`
//     //       }
//     //     },
//     //baseURL: 'localhost:5000'
//  });
 
export const UserAPI = {
    getCurrent: function() {
        return fetch('/api/user/current')
        .then((response) => {
          return response.json();
        })
        .then((data) => {
          return data;
        });
        // return axiosInstance.request({
        //     method: "GET",
        //     url: `/api/user/current`
        // }).then( response => {
        //     return response.data.name
        // });
    }
}