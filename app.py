from flask import Flask, render_template, request, redirect, url_for
from twython import Twython, TwythonError
from twarkov import *
import os

app = Flask(__name__)


# twitter api setup
APP_KEY = os.environ.get('APP_KEY')
APP_SECRET = os.environ.get('APP_SECRET')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')

twitter = Twython(APP_KEY, APP_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


# scrape a timeline, create a markov generator, make a tweet
def get_tweets(user):
    try:
        user_timeline = twitter.get_user_timeline(
            screen_name=user, count=200, include_rts=False, exclude_replies=True)
        tweets = [user_timeline[i]['text']
                  for i in range(len(user_timeline) - 1)]
        return tweets
    except TwythonError as e:
        print e
        return e


def make_tweet(user):
    timeline = ' '.join(get_tweets(user))
    try:
        gen = MarkovGenerator(timeline, 1, tokenize_fun=twitter_tokenize)
        return gen.generate_tweet().lower()
    except ValueError as e:
        print e
        pass


# routing
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate_tweet():
    username = request.form['username']
    tweet = make_tweet(username)
    return render_template('index.html', tweet=tweet)


# run the app
if __name__ == '__main__':
    #app.run(debug=True)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
