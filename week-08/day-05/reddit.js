'use strict';
let redditRequest = new XMLHttpRequest();
let mainSection = document.querySelector('section.posts');
let url = 'http://secure-reddit.herokuapp.com/simple/posts'

talkToAPI('GET', url, null, listPosts);

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
        createHTML(element.score, element.url, element.title, calculateTime(element.timestamp), element.user, element.id);
    });
    // let removers = document.querySelectorAll('a.remove');
    // removers.forEach(function(element){
    //     element.addEventListener('click', function(){
    //         talkToAPI('DELETE', url, null, del)
    //     });
    // });
    createVoters();
}

function createVoters(){
    let upvoters = document.querySelectorAll('img.upvote');
    let downvoters = document.querySelectorAll('img.downvote');
    upvoters.forEach(function(element, i){
        let id = 0;
        if (element.className.length > 10){
            id = element.className.slice(element.className.length-2);
            
        } else {
            id = element.className[element.className.length-1];
        }
        element.addEventListener('click', function(){
            talkToAPI('PUT', url + '/' + id + '/upvote', null, upVote);
        });
        downvoters[i].addEventListener('click', function(){
            talkToAPI('PUT', url + '/' + id + '/downvote', null, downVote);
        });
    });
}

function createHTML (score, url, title, timestamp, user, id) {
    let post = document.createElement('div');
    post.classList.add('post');
    let username = user;
    if (username === null) {
        username = 'anonymus'
    }
    post.innerHTML = `<div class="voter">
                        <img class="upvote id${id}" src="assets/upvote.png"/>
                        <span class="id${id}">${score}</span>
                        <img class="downvote id${id}" src="assets/downvote.png"/>
                     </div>
                     <div class="post-content">
                       <a href="${url}">${title}</a>
                       <p>submitted ${timestamp} mins ago by ${username}</p>
                       <a class="options" href="">Modify</a>
                       <a class="options remove">Remove</a>
                    </div>`;
    mainSection.appendChild(post);
}

function calculateTime (timestamp) {
    let elapsedTime = Math.floor(timestamp/1000/60);
    return elapsedTime;
}

function postPost(json){
    window.location.href = 'reddit.html';
}

function upVote(json){
    let score = document.querySelector('span.id' + json.id);
    let upArrow = document.querySelector('.upvote.id' + json.id);
    score.textContent = json.score
    upArrow.setAttribute('src', 'assets/upvoted.png');
    setTimeout(function(){
        upArrow.setAttribute('src', 'assets/upvote.png'); 
    }, 500);
}

function downVote(json){
    let score = document.querySelector('span.id' + json.id);
    let downArrow = document.querySelector('.downvote.id' + json.id);
    score.textContent = json.score
    downArrow.setAttribute('src', 'assets/downvoted.png');
    setTimeout(function(){
        downArrow.setAttribute('src', 'assets/downvote.png'); 
    }, 500);
}

// function del(json){
//     console.log(json);
// }

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