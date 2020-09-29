### Simple web app that displays recipes and related Twitter quotes


1. Create a developer account on Twitter to get the access keys and tokens. [Sign-up here!](https://developer.twitter.com/en/apply-for-access)
2. Create a Spoonacular account to get an access key. Click [here](https://spoonacular.com/food-api/console#Dashboard) to sign up!
   
   __Important:__ Keep your access keys and tokens safely hidden. Treat them like your passwords.

3. Install flask, tweepy, and dotenv module using the command in your terminal:
```bash
sudo pip install tweepy
sudo pip install flask
sudo pip install python-dotenv
```

4. Clone this repository using the following command in your terminal:
```bash
git clone https://github.com/NJIT-CS490/project1-bcs32
```

5. Do not add your keys in your source code instead create a 2 new root-level file named _tweet.env_ and _spoonacular.env_ to save your keys. In your _tweet.env_ type:
```text
export KEY='TODO'
export SECRET='TODO'
export TOKEN='TODO'
export SECRET_TOKEN='TODO'
```
In your _spoonacular.env_ type:
```text
export SPOONACULAR_KEY='TODO'
```
 Replace TODO with the appropriate keys. Save the file.
 For additional info check [Tweepy documentation.](http://docs.tweepy.org/en/v3.5.0/auth_tutorial.html) and [Spooncular](https://spoonacular.com/food-api/docs#Authentication).

6. Run your code in your terminal.
```python
python get_tweet.py
```

7. Create your own repository on your Github account. 

   __Important:__ Do not push the _tweet.env_ and _spoonacular.env_ to Git.
 
8. Add your code and .gitignore to your repository.
 ```bash
git remote remove origin 
git remote add origin https://github.com/[your-username]/[your-repo-name]
git commit -am "Add get tweet files with and .gitignore"
git push origin master
 ```
 
9. When prompted, enter your Github credentials. Refresh your Github page and you should be able to see your code there.

------------------

##### When deploying the app to Heroku, a cloud platform that hosts web applications

1. Sign up to [Heroku](https://signup.heroku.com/)!

2. Type the following command in your terminal, enter Heroku credentials when prompt:
```bash
nvm i v8
npm install -g heroku
heroku login -i
heroku create
```
3. Click the link (see below) that ends in __herokuapp.com__, this is now the name of your app's webpage.
 ![alt text](https://github.com/bellesune/lect7/blob/master/static/Inkedheroku-site_LI.jpg?raw=true)

   Once you opened it, it should look like this:
   
![alt text](https://github.com/bellesune/lect7/blob/master/static/heroku-welcome.jpg?raw=true)

4. Login to [Heroku](https://id.heroku.com/login) and click the name of your webpage. 
5. Go to Settings and look for __Config Vars__, click 'Reveal Config Vars'. 
Add your access keys in here, the key variables should be the same which can be found in your _tweet.env_ and _spoonacular.env_file (see below).

```text
 KEY 
 SECRET 
 TOKEN 
 SECRET_TOKEN
 SPOONACULAR_KEY
```

6. Go back to your terminal and type the following commands.
```bash
git pull origin master
git push origin master
git push heroku master
```
Click the link of your Heroku webpage, you should be able to see a functional web app called Sippin'.
 
-------------------

### Troubleshooting some common technical issues

##### Command not found while installing module (flask, tweepy, dotenv) in terminal

+ pip command will install the packages in Python. When this error (see below) occurs it means that the executable path is not in PATH variable.
```bash
sudo: pip: command not found
```
+ Go to the root directory and add the executable path to PATH variable.
```bash
cd ~
which pip
```
+ Copy (ctrl + c) the output of _which pip_ and open a text editor (vim).
```bash
vim .bashrc
```
+ When the text editor opens, look for 'export PATH=$PATH:$HOME..../bin:', this should be on the first few lines but this might be different in your local machine. At the very end of this line paste (ctrl + v) the output of 'which pip' to the end of PATH, don't add any space. Save and quit the .bashrc by typing ':wq'.
In your terminal, source the .bashrc:
```bash
source ~/.bashrc
```
+ Try one of the following command again:
```bash
pip install [module]
sudo pip install [module]
```
Resources: [AskUbuntu](https://askubuntu.com/questions/885479/pip-is-apparently-installed-but-not-working)

#####  Internal Server Error (Twitter)

When getting the Internal Server Error when opening running the page, the server is preventing the page to load because of incorrect permission. Most common mistakes are in the access keys provided. Check the following:

+ Double check the spelling of __KEY, SECRET, TOKEN, SECRET_TOKEN__ in _tweet.env_ and  this should all match in the get_tweet.py
+ Make sure the _tweet.env_ matches the text in .gitignore
+ Check your Twitter keys in your [Twitter account dashboard](https://developer.twitter.com/en/portal/dashboard), copy and paste the keys again, it is possible you copied the wrong key to another variable

##### Internal Server Error (Spoonacular)

Searching for recipes that Spoonacular cannot find will result in Internal Server Error. How I fixed it:

+ By analyzing the errors in the server side, Python would throw a ValueError when it receives an inappropriate value
+ Instead of displaying the Internal Server Error (the user might think the app is broken) when not getting a result, displaying a message such as "Invalid recipe" would be better
+ I can raise an exception to ValueError when Spoonacular returns an empty result
+ Searching for invalid keywords or non-existent recipes like "qwerty" would result in:
```bash 
{ "results": [],
  "offset": 0,
  "number": 0,
  "totalResults": 0, }
```
+ By analyzing the json file, we can tell if Spoonacular did not find the recipe, if the results are empty and totalResults is zero. The client side would display either a error message or the recipe base on totalResults. 

Resources: [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError) and [Try-except](https://pythonbasics.org/try-except/)

------------------------
### Known problems

##### Retweeting the same tweet

When viewing the tweets on the webpage, some users retweet the same tweets hence resulting the same tweets in the page. This can be solved by picking a user who did not retweet the previous tweet.
Tweets has an attribute entities which includes mentions, tagging a user. We can filter the tweets by collecting the username of tweets and get the tweet's mention/s (if any) and compare if it matches to any in the username list.

Resources: [Tweet object documentation](https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/overview/tweet-object) and [Entities object documentation](https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/overview/entities-object)

##### Not restricted to only cocktail recipes

When searching for recipes, the app will let you search for any recipes available in Spooncular which contradicts the theme of the app. 
This can be solved by filtering the search by DishType using the ComplexSearch and setting the addRecipeInformation to true. 
The query being searched should be checked if the DishType is in ["beverage", "drink"]. 

Resources: [Spoonacular Search Recipe](https://spoonacular.com/food-api/docs#Search-Recipes-Complex)

----------------------

### What needs improvement

##### Optimizing Spoonacular points

Spoonacular API keeps track of the number of the requests and responses from each endpoint. With a limited 150 points per day, we need to use an endpoint that most likely return all the details we need. 
This app would requests from 2 endpoints, ComplexSearch (1.035 points) and Get Recipe Information (1 point), which would have cost 2.035 each recipe search. 
We can save more points if we use the basic search with no parameters (0 point) and by extracting URL (1 point). The basic search would give us the minor details such as id, title, prep time, serving and source URL and 
extracting from website can give us image, steps, and ingredients. Thus, spending only 1 point per request.

Resources: [Quotas](https://spoonacular.com/food-api/docs#Quotas), [Points](https://spoonacular.com/food-api/docs#Search-Recipes-Complex), and [Extract Recipe From Website](https://spoonacular.com/food-api/docs#Extract-Recipe-from-Website)