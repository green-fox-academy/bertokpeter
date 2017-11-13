'use strict';

const ajax = new XMLHttpRequest();
const body = document.querySelector('body');
let url = "http://localhost:3000";

function talkToAPI(method, resource, callback){
    ajax.open(method, url + resource, true);
    ajax.onload = function(){
        callback(ajax.response);
    }
    ajax.send();
}

talkToAPI('GET', '/list', createList);

function createList(response){
    const list = document.querySelector('div.list');
    list.innerHTML = response;
    talkToAPI('GET', '/all', createTable);
}

function createTable(response){
    const table = document.querySelector('div.table');
    table.innerHTML = response;
}