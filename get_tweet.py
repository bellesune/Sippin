import os
import flask
from flask import Flask
import random
from flask import request
from model_tweet import Tweet
from model_spoonacular import Spoonacular

APP = Flask(__name__)

@APP.route('/', methods=["GET"])
def index():
    """ Get tweets and recipes """
    
    query = request.args.get("search")
    tweet = Tweet(query)
    spoonacular = Spoonacular(query)
    
    if query == None:
        drink_list = [
            "margarita", 
            "mojito", 
            "moscow mule", 
            "martini", 
            "pina colada", 
            "mint julep", 
            "whiskey sour"]
        drink = random.choice(drink_list)
        query = drink
      
    try:    
      idNum, title, prep_time, serving, image,link, steps, totalResults = spoonacular.get_recipe(query)
      ingredients = spoonacular.get_ingredients(idNum)
      
      name_list, user_list, text_list, time_list = tweet.get_quotes(query)
    
    except ValueError:
      return flask.render_template("index.html", totalResults = 0, query = query)
      
    return flask.render_template(
        "index.html",
        query = query,
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
        ingredients = ingredients,
        totalResults = totalResults
        )

APP.run(
    port = int(os.getenv("PORT", 8080)),   
    host = os.getenv("IP", "0.0.0.0"),
    debug = True
)  