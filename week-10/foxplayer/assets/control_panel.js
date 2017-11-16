'use strict';
const controlPanel = function(){
    const audio = document.querySelector('audio');
    // let onEndAction;
    const rewind = document.querySelector('.rewind');
    const forward = document.querySelector('.forward');
    let forwardClickAction;
    let prevClickAction;

    function playTrack(track){
        audio.setAttribute('src', track.path);
    }

    function addEvents(){
        audio.addEventListener('ended', function(){
            forwardClickAction();
        });
        forward.addEventListener('click',function(){
            forwardClickAction();
        });
        rewind.addEventListener('click', function(){
            prevClickAction();
        });
    }

    // function endEvent(callback){
    //     onEndAction = callback;
    // }

    function nextBtnPressed(callback){
        forwardClickAction = callback;
    }

    function prevBtnPressed(callback){
        prevClickAction = callback;
    }

    addEvents();
    return {
        playTrack,
        nextBtnPressed,
        prevBtnPressed
    }
};