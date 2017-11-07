'use strict';
let redditRequest = new XMLHttpRequest();
let mainSection = document.querySelector('section.posts');

function talkToAPI (method, callback) {
    let url = 'http://secure-reddit.herokuapp.com/simple/posts'
    redditRequest.open(method, url, true);
    redditRequest.setRequestHeader('accept', 'application/json');
    redditRequest.onload = function(){
        let posts = JSON.parse(redditRequest.response);
        console.log(posts)
        callback(posts);
    };
    redditRequest.send();
}

function listPosts(json){
    json.posts.forEach(function(element) {
        createHTML(element.url, element.title, calculateTime(element.timestamp), element.user);
    });
}

function createHTML (url, title, timestamp, user) {
    let post = document.createElement('div');
    post.classList.add('post');
    let username = user;
    if (username === null) {
        username = 'anonymus'
    }
    post.innerHTML = `<div class="voter">
                        <img src="assets/upvote.png"/>
                        <span>0</span>
                        <img src="assets/downvote.png"/>
                     </div>
                     <div class="post-content">
                       <a href="` + url + `">` + title +`</a>
                       <p>submitted ` + timestamp + ` mins ago by ` + username + ` </p>
                       <a class="options" href="">Modify</a>
                       <a class="options" href="">Remove</a></div>`;
    mainSection.appendChild(post);
}

function calculateTime (timestamp) {
    let elapsedTime = Math.floor(timestamp/1000/60);
    return elapsedTime;
}

talkToAPI('GET', listPosts);

let postTitle = document.getElementById('title');
let postUrl = document.getElementById('url');
let submitButton = document.querySelector('button.submit');

submitButton.addEventListener('click',)