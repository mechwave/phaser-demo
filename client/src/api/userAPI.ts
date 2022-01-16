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
const checkForError = response => {
  if (!response.ok) throw Error(response.statusText);
  return response.json();
};

export const UserAPI = {
    getCurrent: function() {
        return fetch('/api/user/current')
        .then(checkForError)
        .then((response) => {
          console.log(response)
          return response;
        })
    }
}