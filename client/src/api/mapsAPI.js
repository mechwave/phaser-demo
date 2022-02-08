import { checkForError } from "./checkForError";
  
export const MapsAPI = {
    getCurrent: function() {
        return fetch('/api/map/random')
        .then(checkForError)
        .then((response) => {
        console.log(response)
        return response;
        })
    }
}