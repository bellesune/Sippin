""" Use spoonacular api to get recipe info """
import os
import random
from os.path import join, dirname
import requests
from dotenv import load_dotenv


class Spoonacular:
    """ get basic details, id, title, prep time, serving, image, link """

    def __init__(self, query):
        """ Initialize the query """
        self.query = query

    def get_recipe(self, query):
        """ Get the basic info of recipe """

        dotenv_path2 = join(dirname(__file__), "spoonacular.env")
        load_dotenv(dotenv_path2)

        spoonacular_key = os.environ["SPOONACULAR_KEY"]

        url = (
            "https://api.spoonacular.com/recipes/complexSearch?query={}&"
            "addRecipeInformation=true&apiKey={}".format(query, spoonacular_key)
        )
        response = requests.get(url)
        json_body = response.json()

        total_results = json_body["totalResults"]
        drink = random.randint(0, total_results - 1)

        id_num = json_body["results"][drink]["id"]
        title = json_body["results"][drink]["title"]
        prep_time = json_body["results"][drink]["readyInMinutes"]
        serving = json_body["results"][drink]["servings"]
        image = json_body["results"][drink]["image"]
        link = json_body["results"][drink]["sourceUrl"]

        steps_num = len(json_body["results"][drink]["analyzedInstructions"][0]["steps"])
        steps = [
            json_body["results"][drink]["analyzedInstructions"][0]["steps"][i]["step"]
            for i in range(0, steps_num)
        ]

        return id_num, title, prep_time, serving, image, link, steps, total_results

    def get_ingredients(self, id_num):
        """ Get ingredients using id, create a second url and request """

        dotenv_path2 = join(dirname(__file__), "spoonacular.env")
        load_dotenv(dotenv_path2)

        spoonacular_key = os.environ["SPOONACULAR_KEY"]

        url2 = (
            "https://api.spoonacular.com/recipes/{}/information?"
            "includeNutrition=false&apiKey={}".format(id_num, spoonacular_key)
        )
        response2 = requests.get(url2)
        json_body2 = response2.json()

        ingredients_len = len(json_body2["extendedIngredients"])
        ingredients = [
            json_body2["extendedIngredients"][i]["original"]
            for i in range(0, ingredients_len)
        ]

        return ingredients
