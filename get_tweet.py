import tweepy
import os
import datetime
from time import strftime
import flask
import random
from flask import request
import requests

#test keys here
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), 'tweet.env')
load_dotenv(dotenv_path)

from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), 'spoonacular.env')
load_dotenv(dotenv_path)

app = flask.Flask(__name__)


#Twitter access keys and tokens, hidden in tweet.env
consumer_key = os.environ['KEY']
consumer_secret = os.environ['SECRET']
access_token = os.environ['TOKEN']
access_token_secret = os.environ['TOKEN_SECRET']

#Spoonacular access key, hidden in spoonacular.env
spoonacular_key = os.environ['SPOONACULAR_KEY']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#get basic details, id, title, prep time, serving, image, link
def get_recipe(query):
    
    url = "https://api.spoonacular.com/recipes/complexSearch?query={}&addRecipeInformation=true&apiKey={}".format(query, spoonacular_key)
    response = requests.get(url)
    json_body = response.json()
    
    totalResults = json_body["totalResults"]
    drink = random.randint(0,totalResults-1)
    
    idNum = json_body["results"][drink]["id"]
    title = json_body["results"][drink]["title"]
    prep_time = json_body["results"][drink]["readyInMinutes"]
    serving = json_body["results"][drink]["servings"]
    image = json_body["results"][drink]["image"]
    link = json_body["results"][drink]["sourceUrl"]
    
    steps_num = len(json_body["results"][drink]["analyzedInstructions"][0]["steps"])
    steps = [json_body["results"][drink]["analyzedInstructions"][0]["steps"][i]["step"] for i in range(0,steps_num)]
    
    return idNum, title, prep_time, serving, image, link, steps
 
#get ingredients using id, create a second url and request
def get_ingredients(idNum):
    url2 = "https://api.spoonacular.com/recipes/{}/information?includeNutrition=false&apiKey={}".format(idNum, spoonacular_key)
    response2 = requests.get(url2)
    json_body2 = response2.json()
    
    ingredients_len = len(json_body2["extendedIngredients"])
    ingredients = [json_body2["extendedIngredients"][i]["original"] for i in range(0, ingredients_len)]
    
    return ingredients
 
#get tweets from twitter
def get_quotes(query):
  
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
            
    return name_list, user_list, text_list, time_list


@app.route('/', methods=["GET"])
def get_tweet():
    
    #get tweets from search
    query = request.args.get("search")
    
    #add a random drink in the beginning
    if query == None:
        #add featured drinks to page
        drink_list = ["margarita", "mojito", "moscow mule", "martini", "pina colada", "mint julep", "whiskey sour"]
        drink = random.choice(drink_list)
        query = drink
        
    #get details and ingredients of query
    idNum, title, prep_time, serving, image, steps = get_recipe(query)
    ingredients = get_ingredients(idNum)
    
    #get quotes based on query
    name_list, user_list, text_list, time_list = get_quotes(query)
    
    return flask.render_template(
        "index.html",
        name_list = name_list,
        user_list = user_list,
        text_list = text_list,
        time_list = time_list,
        name_len = len(name_list),
        idNum = idNum,
        title = title,
        prep_time = prep_time,
        serving = serving,
        image = image,
        steps = steps,
        link = link,
        ingredients = ingredients
        )

app.run(
    port = int(os.getenv("PORT", 8080)),   
    host = os.getenv("IP", "0.0.0.0")
)  