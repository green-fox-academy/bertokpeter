'use strict';
const trackList = function(playListNumber){
    const tlSection = document.querySelector('.tracklist');
    let trackClickAction;
    let firstTrack;
    let myAjax = ajax();

    function load(){
        myAjax.xml('GET', "http://localhost:5000/playlist-tracks", render);        
    }
        
    function render(list){
        list.tracklist.forEach(function(element, index){
            createTrackElement(element, index);
        });
        highlight(0);
        setFirst(list.tracklist[0].path);
    }

    function createTrackElement(track, index){
        let trackDiv = document.createElement('div');
        trackDiv.classList.add('track');
        tlSection.appendChild(trackDiv);
        let trackNumber = document.createElement('p');
        trackNumber.textContent = (index+1);
        trackNumber.classList.add('number');
        trackDiv.appendChild(trackNumber);
        let trackTitle = document.createElement('p');
        trackTitle.textContent = track.title;
        trackTitle.classList.add('tracktitle');
        trackDiv.appendChild(trackTitle);
        if (index === 0){
            trackDiv.classList.add('odd');
        } else {
            trackDiv.classList.add('even');
        }
        addEvetns(trackDiv, track.path, index)
    }

    function highlight(index){
        let tracklistDivs = tlSection.querySelectorAll('div.track');
        tracklistDivs.forEach(function(element){
            element.classList.remove('highlighted');
        });
        tracklistDivs[index].classList.add('highlighted');
    }

    function addEvetns(object, path, index){
        object.addEventListener('click', function(){
            trackClickAction(path);
            highlight(index);
        });
    }

    function clickHandler(callback){
        trackClickAction = callback;
    }

    function setFirst(path){
        firstTrack(path);
    }

    function firstHandler(callback){
        firstTrack = callback;
    }
    
    return {
        firstHandler,
        clickHandler,
        load,
        activeTrack: 1
    }
};