'use strict';

const xml = new XMLHttpRequest();
const body = document.querySelector('body');
let url = "http://localhost:3000";

function talkToAPI(method, resource, callback){
    xml.open(method, url + resource, true);
    xml.onload = function(){
        callback(xml.response);
    }
    xml.send();
}

talkToAPI('GET', '/list', createList);

function createList(response){
    const list = document.querySelector('div.list');
    list.innerHTML = response;
    talkToAPI('GET', '/all?plt=340', createTable);
}

function createTable(response){
    const table = document.querySelector('div.table');
    table.innerHTML = response;
}