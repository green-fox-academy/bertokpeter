'use strict';
const playlists = function(){
    const plSection = document.querySelector('section.playlists');

    function load(json){
        let responseList = json;
        render(responseList);
    }

    function render(list){
        list.playlists.forEach(function(element, i){
            createPlaylistElement(element, i);
        });
    }

    function createPlaylistElement(playlist, index){
        let playlistDiv = document.createElement('div');
        playlistDiv.classList.add('playlist');
        plSection.appendChild(playlistDiv);
        let playlistTitle = document.createElement('p');
        playlistTitle.textContent = playlist.title;
        playlistDiv.appendChild(playlistTitle);
        if (playlist.system === 0){
            let playlistX = document.createElement('div');
            playlistX.textContent = 'x';
            playlistDiv.appendChild(playlistX);
        }
        if (index%2 === 0){
            playlistDiv.style.backgroundColor = '#b4b4b4';
        } else {
            playlistDiv.style.backgroundColor = 'white';
        }
    }

    return {
        load
    }
};