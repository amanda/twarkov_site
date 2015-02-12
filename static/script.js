function sendUsername(evt) {
  var f = document.getElementsByTagName('input')[0];
  var req = new XMLHttpRequest();
  req.open("POST", "/generate", true);
  req.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  req.send("username=" + f.value);
  evt.preventDefault();
  req.onreadystatechange = function () {
    if (req.readyState == 4 && req.status == 200) {
      var data = JSON.parse(req.responseText);
      document.getElementById("tweet").innerText=data.tweet;
      var tweetButton = document.getElementsByClassName('twitter-share-button')[0];
      tweetButton.setAttribute("data-text", data.tweet);
      shareButton();
      }
    }
};

var b = document.getElementsByTagName('button')[0];
b.addEventListener("click", sendUsername);

function shareButton () {
    window.twttr=(function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],t=window.twttr||{};if(d.getElementById(id))return;js=d.createElement(s);js.id=id;js.src="https://platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);t._e=[];t.ready=function(f){t._e.push(f);};return t;}(document,"script","twitter-wjs"));
};
