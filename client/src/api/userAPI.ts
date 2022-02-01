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