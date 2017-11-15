'use strcit';

class App {
    constructor(){
        const myAjax = ajax();
        const myPlaylists = playlists();
        myAjax.talkToAPI('GET', "http://localhost:5000/playlists", null, myPlaylists.load);
    }
}

const application = new App();