# twarkov_site
web app for playing with twarkov, my markov text generator for twitter: [twarkov.herokuapp.com](twarkov.herokuapp.com). enter your twitter handle (or a friend's) and get a tweet based on your timeline, then post it to twitter!

## usage
1. clone the repo
2. install requirements with pip: ```pip install -r requirements.txt```
2. run ```python app.py``` and head to localhost:5000 in your favorite browser
3. enter yout twitter handle and see your new tweets!

## todo
- error checking for if username entered doesn't exist (right now nothing happens)
- ~~routing issue: refreshing /generate should take you back to index~~
