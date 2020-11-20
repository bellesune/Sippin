import os
import requests
import random
from os.path import join, dirname
from dotenv import load_dotenv

class Spoonacular:
    """ get basic details, id, title, prep time, serving, image, link """
    
    def __init__(self, query):
        """ Initialize the query """
        self.query = query
    
    def get_recipe(self, query):
        """ Get the basic info of recipe """
        
        dotenv_path2 = join(dirname(__file__), 'spoonacular.env')
        load_dotenv(dotenv_path2)
        
        spoonacular_key = os.environ['SPOONACULAR_KEY']
        
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
        
        return idNum, title, prep_time, serving, image, link, steps, totalResults
     
    def get_ingredients(self, idNum):
        """ Get ingredients using id, create a second url and request """
        
        dotenv_path2 = join(dirname(__file__), 'spoonacular.env')
        load_dotenv(dotenv_path2)
        
        spoonacular_key = os.environ['SPOONACULAR_KEY']
        
        url2 = "https://api.spoonacular.com/recipes/{}/information?includeNutrition=false&apiKey={}".format(idNum, spoonacular_key)
        response2 = requests.get(url2)
        json_body2 = response2.json()
        
        ingredients_len = len(json_body2["extendedIngredients"])
        ingredients = [json_body2["extendedIngredients"][i]["original"] for i in range(0, ingredients_len)]
        
        return ingredients
