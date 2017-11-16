'use strict';
const trackInfo = function(){
    const infoSection = document.querySelector('section.info');
    const trackTitle = infoSection.querySelector('p.title');
    const trackPerformer = infoSection.querySelector('p.performer');
    const favStar = infoSection.querySelector('.icons img');

    function display(track){
        trackTitle.textContent = track.title;
        trackPerformer.textContent = track.artist;
    }

    return {
        display
    }
}