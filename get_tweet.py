import tweepy
import os
import datetime
from time import strftime
import flask
import random

from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), 'tweet.env')
load_dotenv(dotenv_path)

app = flask.Flask(__name__)

#Twitter access keys and tokens, hidden in tweet.env
consumer_key = os.environ['KEY']
consumer_secret = os.environ['SECRET']
access_token = os.environ['TOKEN']
access_token_secret = os.environ['TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

@app.route('/')
def get_tweet():
    
    #get tweets from search
    query = "drink " 
    drink_list = ["margarita", "mojito", "moscow mule", "martini", "mai tai", "whiskey sour", "gimlet", "jello shot", "negroni"]
    drink = random.choice(drink_list)
    query += drink
    drink_list.remove(drink)
    
    #request tweets using keyword in full text and english
    get_tweets = api.search(query, lang='en', tweet_mode='extended')
    
    #display 3 tweets
    counter = 0
    name_list = []
    user_list = []
    text_list = []
    time_list = []
    
    for tweet in get_tweets:
        
        #dont repeat the same user
        if counter < 3 and tweet.user.screen_name not in user_list:
            
            name_list.append(tweet.user.name)
            user_list.append(tweet.user.screen_name)
            text_list.append(tweet.full_text)
            time_list.append(tweet.created_at.strftime("%a, %d %b %Y  |  %H:%M"))
            counter += 1
            
    return flask.render_template(
        "index.html",
        name_list = name_list,
        user_list = user_list,
        text_list = text_list,
        time_list = time_list,
        name_len = len(name_list),
        )

app.run(
    port = int(os.getenv("PORT", 8080)),   
    host = os.getenv("IP", "0.0.0.0")
)  