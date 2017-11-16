'use strict';
const trackList = function(playListNumber){
    const tlSection = document.querySelector('.tracklist');
    let trackClickAction;
    let tracks;
    let setFirst;
    let myAjax = ajax();
    let currrentTrack = 0;

    function load(){
        myAjax.xml('GET', "http://localhost:5000/playlist-tracks", render);        
    }
        
    function render(list){
        tracks = list;
        list.tracklist.forEach(function(element, index, ){
            createTrackElement(element, index)
        });
        highlight(0);
        setFirst.forEach(function(callback){
            callback(list.tracklist[0])
        });
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
        if (index%2 === 0){
            trackDiv.classList.add('odd');
        } else {
            trackDiv.classList.add('even');
        }
        addEvetns(trackDiv, track, index)
    }

    function highlight(index){
        let tracklistDivs = tlSection.querySelectorAll('div.track');
        tracklistDivs.forEach(function(element){
            element.classList.remove('highlighted');
        });
        tracklistDivs[index].classList.add('highlighted');
    }

    function addEvetns(object, track, index){
        object.addEventListener('click', function(){
            trackClickAction.forEach(function(callback){
                callback(track);
            });
            highlight(index);
            currrentTrack = index;
        });
    }

    function clickHandler(callbackArray){
        trackClickAction = callbackArray;
    }

    function playNext(){
        if (currrentTrack+1 < tracks.tracklist.length){
            currrentTrack += 1;
            trackClickAction.forEach(function(callback){
                callback(tracks.tracklist[currrentTrack]);
            });
            highlight(currrentTrack);
        }
    }

    function playPrev(){
        if (currrentTrack-1 >= 0){
            currrentTrack -= 1;
            trackClickAction.forEach(function(callback){
                callback(tracks.tracklist[currrentTrack]);
            });
            highlight(currrentTrack);
        }
    }

    function firstHandler(callbackArray){
        setFirst = callbackArray;
    }
    
    return {
        playNext,
        playPrev,
        firstHandler,
        clickHandler,
        load
    }
};