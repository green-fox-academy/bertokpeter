'use strict';
const controlPanel = function(){
    const audio = document.querySelector('audio');

    function playTrack(src){
        audio.setAttribute('src', src);
    }

    return {
        playTrack
    }
};