'use strcit';

class App {
    constructor(){
        const myAjax = ajax();
        const myPanel = controlPanel();
        const myPlayLists = playLists();
        const myTrackList = trackList();
        myAjax.talkToAPI('GET', "http://localhost:5000/playlists", null, myPlayLists.load, setPlaylists);
        let loadTracks = setInterval(function(){
            if(document.querySelectorAll('div.playlist').length > 0){
                myAjax.talkToAPI('GET', "http://localhost:5000/playlist-tracks", null, myTrackList.load, setTracks);
                clearInterval(loadTracks);
            } 
        },0);
        let loadPlay = setInterval(function(){
            if(document.querySelectorAll('div.track').length > 0){
                myPanel.playTrack(myTrackList.tracks.tracklist[0].path);
                clearInterval(loadPlay);
            }
        },0);

        function setTracks(list){
            myTrackList.tracks = list;
        }

        function setPlaylists(list){
            myPlayLists.playlists = list;
        }
    }
}

const application = new App();