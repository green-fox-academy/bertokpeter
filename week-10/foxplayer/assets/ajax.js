'use strict';
const ajax = function (){
    const playerRequest = new XMLHttpRequest();

    function talkToAPI (method, url, content, callback, setvariable) {
        playerRequest.open(method, url, true);
        playerRequest.onload = function(){
            let list = JSON.parse(playerRequest.response);
            callback(list, setvariable);
        };
        playerRequest.send(JSON.stringify(content));
    }

    return {
        talkToAPI
    }
};