'use strict';
let redditRequest = new XMLHttpRequest();
let mainSection = document.querySelector('section.posts');
let url = 'http://secure-reddit.herokuapp.com/simple/posts'

function talkToAPI (method, url, reqBody, callback) {
    redditRequest.open(method, url, true);
    redditRequest.setRequestHeader('accept', 'application/json');
    if (method === 'POST') {
        redditRequest.setRequestHeader('content-type', 'application/json');
    }
    redditRequest.onload = function(){
        let posts = JSON.parse(redditRequest.response);
        callback(posts);
    };
    redditRequest.send(JSON.stringify(reqBody));
}

function listPosts(json){
    console.log(json);
    json.posts.forEach(function(element) {
        createHTML(element.score, element.url, element.title, calculateTime(element.timestamp), element.user);
    });
    let removers = document.querySelectorAll('a.remove');
    json.posts.forEach(function(element,i){
        removers[i].addEventListener('click', function(){
            talkToAPI('DELETE', url, null, del)
        });
    });
}

function createHTML (score, url, title, timestamp, user) {
    let post = document.createElement('div');
    post.classList.add('post');
    let username = user;
    if (username === null) {
        username = 'anonymus'
    }
    post.innerHTML = `<div class="voter">
                        <img class="upvote" src="assets/upvote.png"/>
                        <span>` + score + `</span>
                        <img class="downvote" src="assets/downvote.png"/>
                     </div>
                     <div class="post-content">
                       <a href="` + url + `">` + title +`</a>
                       <p>submitted ` + timestamp + ` mins ago by ` + username + ` </p>
                       <a class="options" href="">Modify</a>
                       <a class="options remove">Remove</a></div>`;
    mainSection.appendChild(post);
}

function calculateTime (timestamp) {
    let elapsedTime = Math.floor(timestamp/1000/60);
    return elapsedTime;
}

talkToAPI('GET', url, null, listPosts);

let postTitle = document.getElementById('title');
let postUrl = document.getElementById('url');
let submitButton = document.querySelector('button.submit');

submitButton.addEventListener('click', function(){
    let reqBody = {
        "title": postTitle.value,
        "url": postUrl.value
    }
    talkToAPI('POST', url, reqBody, postPost);
});

function postPost(json){
    window.location.href = 'reddit.html';
}

function del(json){
    console.log(json);
}