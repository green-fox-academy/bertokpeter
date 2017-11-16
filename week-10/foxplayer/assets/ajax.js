'use strict';
const ajax = function (){
    const playerRequest = new XMLHttpRequest();

    function xml(method, url, callback, content=null) {
        playerRequest.open(method, url, true);
        playerRequest.setRequestHeader('accept', 'application/json');
        playerRequest.setRequestHeader('content-type', 'application/json');
        if (method !== 'GET'){
            content = JSON.stringify(content);
        }
        playerRequest.onload = function(){
            let list = JSON.parse(playerRequest.response);
            callback(list);
        };
        playerRequest.send(content);
    }

    return {
        xml
    }
};