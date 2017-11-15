'use strict';
const ajax = function (){
    const playerRequest = new XMLHttpRequest();

    function talkToAPI (method, url, content, callback) {
        playerRequest.open(method, url, true);
        playerRequest.onload = function(){
            let list = JSON.parse(playerRequest.response);
            callback(list);
        };
        playerRequest.send(JSON.stringify(content));
    }

    return {
        talkToAPI
    }
};