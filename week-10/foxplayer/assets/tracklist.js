'use strict';
const trackList = function(playListNumber){
    const tlSection = document.querySelector('.tracklist');
    let tracks;

    function load(json, callback){
        tracks = json;
        render(tracks);
        callback(tracks);
    }
        
    function render(list){
        list.tracklist.forEach(function(element, index){
            createTrackElement(element, index);
        });
        highlight(0);
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
    }

    function highlight(index){
        let tracklistDivs = tlSection.querySelectorAll('div.track');
        tracklistDivs[index].classList.toggle('highlighted');
    }

    return {
        load,
        tracks,
        activeTrack: 1
    }
};