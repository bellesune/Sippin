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
    
    # url = "https://api.spoonacular.com/recipes/complexSearch?query={}&addRecipeInformation=true&apiKey={}".format(query, spoonacular_key)
    # response = requests.get(url)
    # json_body = response.json()
    
    json_body = {
        "results": [
    {
      
      "aggregateLikes": 1,
      "spoonacularScore": 5.0,
      "healthScore": 0.0,
      "creditsText": "Foodista.com \u2013 The Cooking Encyclopedia Everyone Can Edit",
      "license": "CC BY 3.0",
      "sourceName": "Foodista",
      "pricePerServing": 280.47,
      "id": 639614,
      "title": "Classic Margarita",
      "readyInMinutes": 5,
      "servings": 1,
      "sourceUrl": "http://www.foodista.com/recipe/NFJSNYXP/classic-margarita",
      "image": "https://spoonacular.com/recipeImages/639614-312x231.jpg",
      "imageType": "jpg",
      "summary": "Classic Margarita might be just the beverage you are searching for. One serving contains <b>147 calories</b>, <b>0g of protein</b>, and <b>0g of fat</b>. This recipe serves 1 and costs $2.8 per serving. From preparation to the plate, this recipe takes approximately <b>5 minutes</b>. This recipe is liked by 1 foodies and cooks. Head to the store and pick up tequila, ice, lime juice, and a few other things to make it today. It is a good option if you're following a <b>gluten free, fodmap friendly, and vegan</b> diet. All things considered, we decided this recipe <b>deserves a spoonacular score of 7%</b>. This score is improvable. Try <a href=\"https://spoonacular.com/recipes/classic-margarita-910643\">Classic Margarita</a>, <a href=\"https://spoonacular.com/recipes/classic-margarita-77466\">Classic Margarita</a>, and <a href=\"https://spoonacular.com/recipes/classic-margarita-696193\">Classic Margarita</a> for similar recipes.",
      "cuisines": [],
      "dishTypes": [
        "beverage",
        "drink"
      ],
      "diets": [
        "gluten free",
        "dairy free",
        "lacto ovo vegetarian",
        "fodmap friendly",
        "vegan"
      ],
      "occasions": [],
      "analyzedInstructions": [
        {
          "name": "",
          "steps": [
            {
              "number": 1,
              "step": "In a cocktail shaker combine all ingredients with ice and shake vigorously. Strain into a salt rimmed stemware glass. No garnish necessary.",
              "ingredients": [
                {
                  "id": 0,
                  "name": "cocktail",
                  "localizedName": "cocktail",
                  "image": "rum-dark.jpg"
                },
                {
                  "id": 0,
                  "name": "shake",
                  "localizedName": "shake",
                  "image": ""
                },
                {
                  "id": 2047,
                  "name": "salt",
                  "localizedName": "salt",
                  "image": "salt.jpg"
                },
                {
                  "id": 10014412,
                  "name": "ice",
                  "localizedName": "ice",
                  "image": "ice-cubes.png"
                }
              ],
              "equipment": []
            }
          ]
        }
      ],
      "spoonacularSourceUrl": "https://spoonacular.com/classic-margarita-639614"
    },
    
   
    {
      
      "aggregateLikes": 1,
      "spoonacularScore": 28.0,
      "healthScore": 4.0,
      "creditsText": "Foodista.com \u2013 The Cooking Encyclopedia Everyone Can Edit",
      "license": "CC BY 3.0",
      "sourceName": "Foodista",
      "pricePerServing": 349.3,
      "id": 661835,
      "title": "Strawberry Margarita",
      "readyInMinutes": 45,
      "servings": 3,
      "sourceUrl": "http://www.foodista.com/recipe/MNSHVB4R/strawberry-margarita",
      "image": "https://spoonacular.com/recipeImages/661835-312x231.jpg",
      "imageType": "jpg",
      "summary": "Strawberry Margarita might be just the beverage you are searching for. This recipe serves 3 and costs $3.49 per serving. One serving contains <b>255 calories</b>, <b>1g of protein</b>, and <b>1g of fat</b>. Head to the store and pick up lime garnish, tequila, strawberries, and a few other things to make it today. It will be a hit at your <b>Mother's Day</b> event. From preparation to the plate, this recipe takes around <b>45 minutes</b>. This recipe from Foodista has 1 fans. It is a good option if you're following a <b>gluten free, fodmap friendly, and vegan</b> diet. All things considered, we decided this recipe <b>deserves a spoonacular score of 31%</b>. This score is not so great. Try <a href=\"https://spoonacular.com/recipes/strawberry-margarita-pie-585649\">Strawberry Margarita Pie</a>, <a href=\"https://spoonacular.com/recipes/strawberry-margarita-pie-516887\">Strawberry Margarita Pie</a>, and <a href=\"https://spoonacular.com/recipes/strawberry-margarita-168441\">Strawberry Margarita</a> for similar recipes.",
      "cuisines": [],
      "dishTypes": [],
      "diets": [
        "gluten free",
        "dairy free",
        "lacto ovo vegetarian",
        "fodmap friendly",
        "vegan"
      ],
      "occasions": [
        "mother's day"
      ],
      "analyzedInstructions": [
        {
          "name": "",
          "steps": [
            {
              "number": 1,
              "step": "In a blender, combine strawberries, tequila, lemonade, Tripe Sec, and ice; blend until smooth.",
              "ingredients": [
                {
                  "id": 9316,
                  "name": "strawberries",
                  "localizedName": "strawberries",
                  "image": "strawberries.png"
                },
                {
                  "id": 99184,
                  "name": "lemonade",
                  "localizedName": "lemonade",
                  "image": "lemonade.jpg"
                },
                {
                  "id": 10814037,
                  "name": "tequila",
                  "localizedName": "tequila",
                  "image": "tequila.png"
                },
                {
                  "id": 10014412,
                  "name": "ice",
                  "localizedName": "ice",
                  "image": "ice-cubes.png"
                }
              ],
              "equipment": [
                {
                  "id": 404726,
                  "name": "blender",
                  "localizedName": "blender",
                  "image": "blender.png"
                }
              ]
            },
            {
              "number": 2,
              "step": "Pour into stemmed Margarita Glasses rimmed with either coarse salt, or coarse sugar.To create a salt or sugar-rimmed glass, take a lime wedge and rub the drinking surface of the glass so it is barely moist. Dip the edge of the glass into coarse salt or sugar.",
              "ingredients": [
                {
                  "id": 10019335,
                  "name": "coarse sugar",
                  "localizedName": "coarse sugar",
                  "image": "sugar-in-bowl.png"
                },
                {
                  "id": 1002047,
                  "name": "coarse salt",
                  "localizedName": "coarse salt",
                  "image": "salt.jpg"
                },
                {
                  "id": 1029159,
                  "name": "lime wedge",
                  "localizedName": "lime wedge",
                  "image": "lime-wedge.jpg"
                },
                {
                  "id": 0,
                  "name": "margarita",
                  "localizedName": "margarita",
                  "image": "rum-dark.jpg"
                },
                {
                  "id": 19335,
                  "name": "sugar",
                  "localizedName": "sugar",
                  "image": "sugar-in-bowl.png"
                },
                {
                  "id": 2047,
                  "name": "salt",
                  "localizedName": "salt",
                  "image": "salt.jpg"
                },
                {
                  "id": 0,
                  "name": "dip",
                  "localizedName": "dip",
                  "image": ""
                },
                {
                  "id": 1012034,
                  "name": "dry seasoning rub",
                  "localizedName": "dry seasoning rub",
                  "image": "seasoning.png"
                }
              ],
              "equipment": []
            },
            {
              "number": 3,
              "step": "Garnish with a whole strawberry",
              "ingredients": [
                {
                  "id": 9316,
                  "name": "strawberries",
                  "localizedName": "strawberries",
                  "image": "strawberries.png"
                }
              ],
              "equipment": []
            },
            {
              "number": 4,
              "step": "Makes 2 to 3 serving.",
              "ingredients": [],
              "equipment": []
            }
          ]
        }
      ],
      "spoonacularSourceUrl": "https://spoonacular.com/strawberry-margarita-661835"
    },
    {
      
      "weightWatcherSmartPoints": 9,
      "gaps": "no",
     
      "aggregateLikes": 3,
      "spoonacularScore": 9.0,
      "healthScore": 0.0,
      "creditsText": "Foodista.com \u2013 The Cooking Encyclopedia Everyone Can Edit",
      "license": "CC BY 3.0",
      "sourceName": "Foodista",
      "pricePerServing": 393.51,
      "id": 643559,
      "title": "Fresh Peach Margarita With Lime Sugar",
      "readyInMinutes": 45,
      "servings": 2,
      "sourceUrl": "http://www.foodista.com/recipe/Y8QJY2B2/fresh-peach-margarita-with-lime-sugar",
      "image": "https://spoonacular.com/recipeImages/643559-312x231.jpg",
      "imageType": "jpg",
      "summary": "Fresh Peach Margarita With Lime Sugar might be just the beverage you are searching for. One serving contains <b>287 calories</b>, <b>1g of protein</b>, and <b>0g of fat</b>. For <b>$3.94 per serving</b>, this recipe <b>covers 3%</b> of your daily requirements of vitamins and minerals. It is a good option if you're following a <b>gluten free and vegan</b> diet. A mixture of silver tequila, sugar, orange liquor, and a handful of other ingredients are all it takes to make this recipe so scrumptious. 3 people have made this recipe and would make it again. From preparation to the plate, this recipe takes about <b>45 minutes</b>. All things considered, we decided this recipe <b>deserves a spoonacular score of 11%</b>. This score is not so tremendous. Try <a href=\"https://spoonacular.com/recipes/fresh-peach-margarita-605965\">Fresh Peach Margarita</a>, <a href=\"https://spoonacular.com/recipes/fresh-peach-jalapeo-margarita-480709\">Fresh Peach Jalape\u00f1o Margarita</a>, and <a href=\"https://spoonacular.com/recipes/fresh-lime-margarita-582002\">Fresh Lime Margarita</a> for similar recipes.",
      "cuisines": [],
      "dishTypes": [],
      "diets": [
        "gluten free",
        "dairy free",
        "lacto ovo vegetarian",
        "vegan"
      ],
      "occasions": [],
      "analyzedInstructions": [
        {
          "name": "If making lime sugar",
          "steps": [
            {
              "number": 1,
              "step": "Add 1/2 teaspoon of finely minced lime zest to 1/4 cup granulated sugar and set aside for about 30 minutes, stirring occasionally.For a pretty presentation, coat the rims of the glasses you are using with lime sugar (of course you can alternatively use plain white sugar).  Do this by rubbing the rim with a lime wedge and then placing the rim into a plate that has the sugar in it until the rim is coated with sugar.",
              "ingredients": [
                {
                  "id": 10719335,
                  "name": "granulated sugar",
                  "localizedName": "granulated sugar",
                  "image": "sugar-in-bowl.png"
                },
                {
                  "id": 1029159,
                  "name": "lime wedge",
                  "localizedName": "lime wedge",
                  "image": "lime-wedge.jpg"
                },
                {
                  "id": 1009159,
                  "name": "lime zest",
                  "localizedName": "lime zest",
                  "image": "zest-lime.jpg"
                },
                {
                  "id": 19335,
                  "name": "sugar",
                  "localizedName": "sugar",
                  "image": "sugar-in-bowl.png"
                },
                {
                  "id": 9159,
                  "name": "lime",
                  "localizedName": "lime",
                  "image": "lime.jpg"
                }
              ],
              "equipment": [],
              "length": {
                "number": 30,
                "unit": "minutes"
              }
            },
            {
              "number": 2,
              "step": "Place all ingredients into the blender and puree.",
              "ingredients": [],
              "equipment": [
                {
                  "id": 404726,
                  "name": "blender",
                  "localizedName": "blender",
                  "image": "blender.png"
                }
              ]
            },
            {
              "number": 3,
              "step": "Add a little cold water if it is too thick.  Either chill all ingredients before making or add some ice cubes after you have made the margarita and stir it until it is as cold as you like and strain it into your glasses (or serve on the rocks).",
              "ingredients": [
                {
                  "id": 10014412,
                  "name": "ice cubes",
                  "localizedName": "ice cubes",
                  "image": "ice-cubes.png"
                },
                {
                  "id": 0,
                  "name": "margarita",
                  "localizedName": "margarita",
                  "image": "rum-dark.jpg"
                },
                {
                  "id": 14412,
                  "name": "water",
                  "localizedName": "water",
                  "image": "water.png"
                }
              ],
              "equipment": []
            }
          ]
        }
      ],
      "spoonacularSourceUrl": "https://spoonacular.com/fresh-peach-margarita-with-lime-sugar-643559"
    },
    {
      
      "aggregateLikes": 1,
      "spoonacularScore": 5.0,
      "healthScore": 0.0,
      "creditsText": "Foodista.com \u2013 The Cooking Encyclopedia Everyone Can Edit",
      "license": "CC BY 3.0",
      "sourceName": "Foodista",
      "pricePerServing": 231.18,
      "id": 660398,
      "title": "Smokin' Good Margarita",
      "readyInMinutes": 45,
      "servings": 1,
      "sourceUrl": "https://www.foodista.com/recipe/244Q7SM6/smokin-good-margarita",
      "image": "https://spoonacular.com/recipeImages/660398-312x231.jpg",
      "imageType": "jpg",
      "summary": "Smokin' Good Margarita could be just the <b>gluten free, dairy free, lacto ovo vegetarian, and fodmap friendly</b> recipe you've been looking for. This recipe makes 1 servings with <b>129 calories</b>, <b>0g of protein</b>, and <b>0g of fat</b> each. For <b>$2.31 per serving</b>, this recipe <b>covers 1%</b> of your daily requirements of vitamins and minerals. 1 person were impressed by this recipe. If you have del maguey chichicapa mezcal, grand marnier, squeezed lime juice, and a few other ingredients on hand, you can make it. It is brought to you by Foodista. It works well as a beverage. From preparation to the plate, this recipe takes around <b>around 45 minutes</b>. Taking all factors into account, this recipe <b>earns a spoonacular score of 1%</b>, which is improvable. Similar recipes include <a href=\"https://spoonacular.com/recipes/smokin-spiced-corn-381116\">Smokin' Spiced Corn</a>, <a href=\"https://spoonacular.com/recipes/smokin-potato-salad-289186\">Smokin' Potato Salad</a>, and <a href=\"https://spoonacular.com/recipes/smokin-hoppin-john-204694\">Smokin' Hoppin' John</a>.",
      "cuisines": [],
      "dishTypes": [
        "beverage",
        "drink"
      ],
      "diets": [
        "gluten free",
        "dairy free",
        "lacto ovo vegetarian",
        "fodmap friendly",
        "vegan"
      ],
      "occasions": [],
      "analyzedInstructions": [
        {
          "name": "",
          "steps": [
            {
              "number": 1,
              "step": "First, prepare your glasses.",
              "ingredients": [],
              "equipment": []
            },
            {
              "number": 2,
              "step": "Pour a 4 inch circle of kosher salt on a plate, run an open lime around the rim of the glass and then dip the rim of the glass in the salt.",
              "ingredients": [
                {
                  "id": 1082047,
                  "name": "kosher salt",
                  "localizedName": "kosher salt",
                  "image": "salt.jpg"
                },
                {
                  "id": 9159,
                  "name": "lime",
                  "localizedName": "lime",
                  "image": "lime.jpg"
                },
                {
                  "id": 2047,
                  "name": "salt",
                  "localizedName": "salt",
                  "image": "salt.jpg"
                },
                {
                  "id": 0,
                  "name": "dip",
                  "localizedName": "dip",
                  "image": ""
                }
              ],
              "equipment": []
            },
            {
              "number": 3,
              "step": "Let it dry for a minute or two.  Be careful when adding ice to the glass - you don't want to knock the salt off the rim.",
              "ingredients": [
                {
                  "id": 2047,
                  "name": "salt",
                  "localizedName": "salt",
                  "image": "salt.jpg"
                },
                {
                  "id": 10014412,
                  "name": "ice",
                  "localizedName": "ice",
                  "image": "ice-cubes.png"
                }
              ],
              "equipment": []
            },
            {
              "number": 4,
              "step": "Combine all ingredients in a cocktail shaker with crushed ice, shake and strain into your prepared glass.  Then, pour a tablespoon or so of the Del Maguey Chichicapa Mezcal over the top.  Finally, garnish with a lime, serve, and let the Margarita Madness begin!",
              "ingredients": [
                {
                  "id": 10114412,
                  "name": "crushed ice cubes",
                  "localizedName": "crushed ice cubes",
                  "image": "crushed-ice.png"
                },
                {
                  "id": 0,
                  "name": "margarita",
                  "localizedName": "margarita",
                  "image": "rum-dark.jpg"
                },
                {
                  "id": 0,
                  "name": "cocktail",
                  "localizedName": "cocktail",
                  "image": "rum-dark.jpg"
                },
                {
                  "id": 11014037,
                  "name": "mezcal",
                  "localizedName": "mezcal",
                  "image": "tequila.png"
                },
                {
                  "id": 0,
                  "name": "shake",
                  "localizedName": "shake",
                  "image": ""
                },
                {
                  "id": 9159,
                  "name": "lime",
                  "localizedName": "lime",
                  "image": "lime.jpg"
                }
              ],
              "equipment": []
            }
          ]
        }
      ],
      "spoonacularSourceUrl": "https://spoonacular.com/smokin-good-margarita-660398"
    }
  ],
  "offset": 0,
  "number": 10,
  "totalResults": 6
}
    
    drink = 1 #drink index
    
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
    # url2 = "https://api.spoonacular.com/recipes/{}/information?includeNutrition=false&apiKey={}".format(idNum, spoonacular_key)
    # response2 = requests.get(url2)
    # json_body2 = response2.json()
    
    json_body2 = {
  
  "aggregateLikes": 1,
  "spoonacularScore": 5.0,
  "healthScore": 0.0,
  "creditsText": "Foodista.com \u2013 The Cooking Encyclopedia Everyone Can Edit",
  "license": "CC BY 3.0",
  "sourceName": "Foodista",
  "pricePerServing": 280.47,
  "extendedIngredients": [
    {
      "id": 10014412,
      "aisle": "Frozen",
      "image": "ice-cubes.png",
      "consistency": "solid",
      "name": "ice",
      "original": "Ice",
      "originalString": "Ice",
      "originalName": "Ice",
      "amount": 1.0,
      "unit": "serving",
      "meta": [],
      "metaInformation": [],
      "measures": {
        "us": {
          "amount": 1.0,
          "unitShort": "serving",
          "unitLong": "serving"
        },
        "metric": {
          "amount": 1.0,
          "unitShort": "serving",
          "unitLong": "serving"
        }
      }
    },
    {
      "id": 9160,
      "aisle": "Produce",
      "image": "lime-juice.png",
      "consistency": "liquid",
      "name": "lime juice",
      "original": "1 ounce lime juice",
      "originalString": "1 ounce lime juice",
      "originalName": "lime juice",
      "amount": 1.0,
      "unit": "ounce",
      "meta": [],
      "metaInformation": [],
      "measures": {
        "us": {
          "amount": 1.0,
          "unitShort": "oz",
          "unitLong": "ounce"
        },
        "metric": {
          "amount": 28.35,
          "unitShort": "g",
          "unitLong": "grams"
        }
      }
    },
    {
      "id": 90480,
      "aisle": "Alcoholic Beverages",
      "image": "simple-syrup.jpg",
      "consistency": "liquid",
      "name": "simple syrup",
      "original": "1/2 teaspoon simple syrup",
      "originalString": "1/2 teaspoon simple syrup",
      "originalName": "simple syrup",
      "amount": 0.5,
      "unit": "teaspoon",
      "meta": [],
      "metaInformation": [],
      "measures": {
        "us": {
          "amount": 0.5,
          "unitShort": "tsps",
          "unitLong": "teaspoons"
        },
        "metric": {
          "amount": 0.5,
          "unitShort": "tsps",
          "unitLong": "teaspoons"
        }
      }
    },
    {
      "id": 10814037,
      "aisle": "Alcoholic Beverages",
      "image": "tequila.png",
      "consistency": "liquid",
      "name": "tequila",
      "original": "2 ounces Tequila",
      "originalString": "2 ounces Tequila",
      "originalName": "Tequila",
      "amount": 2.0,
      "unit": "ounces",
      "meta": [],
      "metaInformation": [],
      "measures": {
        "us": {
          "amount": 2.0,
          "unitShort": "oz",
          "unitLong": "ounces"
        },
        "metric": {
          "amount": 56.699,
          "unitShort": "g",
          "unitLong": "grams"
        }
      }
    },
    {
     
      "name": "cointreau",
      "original": "1 ounce Cointreau",
      "originalString": "1 ounce Cointreau",
      "originalName": "Cointreau",
      "amount": 1.0,
      "unit": "ounce",
      "meta": [],
      "metaInformation": [],
      "measures": {
        "us": {
          "amount": 1.0,
          "unitShort": "oz",
          "unitLong": "ounce"
        },
        "metric": {
          "amount": 28.35,
          "unitShort": "g",
          "unitLong": "grams"
        }
      }
    }
  ],
  "id": 639614,
  "title": "Classic Margarita",
  "readyInMinutes": 5,
  "servings": 1,
  "sourceUrl": "http://www.foodista.com/recipe/NFJSNYXP/classic-margarita",
  "image": "https://spoonacular.com/recipeImages/639614-556x370.jpg",
  "imageType": "jpg",
  "summary": "Classic Margarita might be just the beverage you are searching for. One serving contains <b>147 calories</b>, <b>0g of protein</b>, and <b>0g of fat</b>. This recipe serves 1 and costs $2.8 per serving. From preparation to the plate, this recipe takes approximately <b>5 minutes</b>. This recipe is liked by 1 foodies and cooks. Head to the store and pick up tequila, ice, lime juice, and a few other things to make it today. It is a good option if you're following a <b>gluten free, fodmap friendly, and vegan</b> diet. All things considered, we decided this recipe <b>deserves a spoonacular score of 7%</b>. This score is improvable. Try <a href=\"https://spoonacular.com/recipes/classic-margarita-910643\">Classic Margarita</a>, <a href=\"https://spoonacular.com/recipes/classic-margarita-77466\">Classic Margarita</a>, and <a href=\"https://spoonacular.com/recipes/classic-margarita-696193\">Classic Margarita</a> for similar recipes.",
  "cuisines": [],
  "dishTypes": [
    "beverage",
    "drink"
  ],
  "diets": [
    "gluten free",
    "dairy free",
    "lacto ovo vegetarian",
    "fodmap friendly",
    "vegan"
  ],
  "occasions": [],
  "winePairing": {},
  "instructions": "<ol><li>In a cocktail shaker combine all ingredients with ice and shake vigorously. Strain into a salt rimmed stemware glass. No garnish necessary.</li></ol>",
  "analyzedInstructions": [
    {
      "name": "",
      "steps": [
        {
          "number": 1,
          "step": "In a cocktail shaker combine all ingredients with ice and shake vigorously. Strain into a salt rimmed stemware glass. No garnish necessary.",
          "ingredients": [
            {
              "id": 0,
              "name": "cocktail",
              "localizedName": "cocktail",
              "image": "rum-dark.jpg"
            },
            {
              "id": 0,
              "name": "shake",
              "localizedName": "shake",
              "image": ""
            },
            {
              "id": 2047,
              "name": "salt",
              "localizedName": "salt",
              "image": "salt.jpg"
            },
            {
              "id": 10014412,
              "name": "ice",
              "localizedName": "ice",
              "image": "ice-cubes.png"
            }
          ],
          "equipment": []
        }
      ]
    }
  ],
  
  "spoonacularSourceUrl": "https://spoonacular.com/classic-margarita-639614"
} 
    
    ingredients_len = len(json_body2["extendedIngredients"])
    ingredients = [json_body2["extendedIngredients"][i]["original"] for i in range(0, ingredients_len)]
    
    return ingredients
    

@app.route('/', methods=["GET"])
def get_tweet():
    
    #get tweets from search
    query = request.args.get("search")
    
    if query == None:
        #add featured drinks to page
        drink_list = ["margarita", "mojito", "moscow mule", "martini", "pina colada", "mint julep", "whiskey sour"]
        drink = random.choice(drink_list)
        query = drink
        
    #get details and ingredients of query
    idNum, title, prep_time, serving, image, link, steps = get_recipe(query)
    ingredients = get_ingredients(idNum)
    
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