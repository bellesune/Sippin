import tweepy
import os
import datetime
from time import strftime

#Twitter access keys and tokens, hidden in tweet.env
consumer_key = os.environ['KEY']
consumer_secret = os.environ['SECRET']
access_token = os.environ['TOKEN']
access_token_secret = os.environ['TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#get tweets from search, 
query = "drink "      #hard code relevant keyword here
query += "margarita"  #add type recipe keywords here

print("Getting tweets...")
print()

#request tweets using keyword in full text and english
get_tweets = api.search(query, lang='en', tweet_mode='extended')

counter = 0
user_list = []

#display 3 tweets
for tweet in get_tweets:
    
    #dont repeat the same user
    if counter < 3 and tweet.user.screen_name not in user_list:
        
        print(tweet.user.name)
        print("@" + tweet.user.screen_name)
        print(tweet.full_text)
        print(tweet.created_at.strftime("%a, %d %b %Y %H:%M:%S"))
        print()
        
        user_list.append(tweet.user.screen_name)
        counter += 1

print(user_list)