'use strict';
// Accidentally I got the wrong URL for a funny subreddit. It's probably "odds" and not "bots"
// Also, the URL is missing a crutial component, find out what it is and insert it too!

let url = "https//www.reddit.com/r/nevertellmethebots";

let index1 = url.indexOf("//");
let index2 = url.indexOf("bots");
url = url.slice(0,index1) + ":" + url.slice(index1, index2) + "odds"; 
console.log(url);