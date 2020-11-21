""" Use Twitter api to retrieve tweets """
import os
from os.path import join, dirname
import tweepy
from dotenv import load_dotenv


class Tweet:
    """ Requests tweets """

    def __init__(self, query):
        """ Initialize the Tweet class """
        self.query = query

    def get_quotes(self, query):
        """ Get the tweets based on query """

        dotenv_path = join(dirname(__file__), "tweet.env")
        load_dotenv(dotenv_path)

        consumer_key = os.environ["KEY"]
        consumer_secret = os.environ["SECRET"]
        access_token = os.environ["TOKEN"]
        access_token_secret = os.environ["TOKEN_SECRET"]

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

        get_tweets = api.search(query, lang="en", tweet_mode="extended")

        counter = 0
        name_list = []
        user_list = []
        text_list = []
        time_list = []

        for tweet in get_tweets:

            if counter < 3 and tweet.user.screen_name not in user_list:

                name_list.append(tweet.user.name)
                user_list.append(tweet.user.screen_name)
                text_list.append(tweet.full_text)
                time_list.append(tweet.created_at.strftime("%a, %d %b %Y  |  %H:%M"))
                counter += 1

        return name_list, user_list, text_list, time_list
