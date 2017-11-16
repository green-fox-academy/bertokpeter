'use strict';
const playLists = function(){
    const plSection = document.querySelector('section.playlists');
    const plAdder = document.querySelector('p.plus');
    const adderDialog = document.querySelector('.adder .dialog');
    const cancelBtn = adderDialog.querySelector('.cancel');
    const okBtn = adderDialog.querySelector('.ok');
    const plInput = adderDialog.querySelector('input');
    let myAjax = ajax();
    let playlistClickAction;

    function load(){
        myAjax.xml('GET', "http://localhost:5000/playlists", render);
    }   

    function render(list){
        plSection.innerHTML = '';
        list.playlists.forEach(function(element, index){
            createPlaylistElement(element, index);
        });
        highlight(0);
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
        if (playlist.id%2 !== 0){
            playlistDiv.classList.add('odd');
        } else {
            playlistDiv.classList.add('even');
        }
        addEvents(playlistDiv, playlist, index);
    }

    function highlight(index){
        let playlistDivs = plSection.querySelectorAll('div.playlist');
        playlistDivs.forEach(function(element){
            element.classList.remove('highlighted');
        });
        playlistDivs[index].classList.add('highlighted');
    }

    function addEvents(object, playlist, index){
        object.addEventListener('click', function(){
            playlistClickAction("/" + playlist.id);
            highlight(index);
        });
    }

    function create(){
        plAdder.addEventListener('click', function(){
            adderDialog.style.display = 'flex';
        });
        cancelBtn.addEventListener('click', function(){
            adderDialog.style.display = 'none';
        });
        okBtn.addEventListener('click', function(){
            let reqBody = {
                "title": plInput.value
            };
            myAjax.xml('POST', "http://localhost:5000/playlists", render, reqBody);
            adderDialog.style.display = 'none';
        });
    }

    function clickHandler(callback){
        playlistClickAction = callback;
    }

    create();
    return {
        load,
        clickHandler
    }
};