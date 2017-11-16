'use strict';
const playLists = function(){
    const plSection = document.querySelector('section.playlists');
    let myAjax = ajax();

    function load(){
        myAjax.xml('GET', "http://localhost:5000/playlists", render);
    }   

    function render(list){
        list.playlists.forEach(function(element){
            createPlaylistElement(element);
        });
        highlight(0);
    }

    function createPlaylistElement(playlist){
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
        if (playlist.id%2 !== 0){
            playlistDiv.classList.add('odd');
        } else {
            playlistDiv.classList.add('even');
        }
    }

    function highlight(index){
        let playlistDivs = plSection.querySelectorAll('div.playlist');
        playlistDivs[index].classList.toggle('highlighted');
    }


    load();
    return {
        load,
        activePlayList: 1,
    }
};