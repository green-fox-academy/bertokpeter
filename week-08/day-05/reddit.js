'use strict';
let redditRequest = new XMLHttpRequest();
let mainSection = document.querySelector('section.posts');
// redditRequest.open()

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
        createHTML(element.url, element.title, calculateTime(element.timestamp));
    });
}

function createHTML (url, title, timestamp) {
    let post = document.createElement('div');
    post.classList.add('post');
    post.innerHTML = `<div class="voter"><img src="assets/upvote.png"/><span>0</span><img src="assets/downvote.png"/>
                     </div><div class="post-content"><a href="` + url + `">` + title +`</a><p>submitted ` + timestamp + ` mins ago by
                     anonymus</p><a href="">Modify</a><a href="">Remove</a></div>`;
    mainSection.appendChild(post);
}

function calculateTime (timestamp) {
    let elapsedTime = Math.floor(timestamp/60);
    return elapsedTime;
}

talkToAPI('GET', listPosts);

