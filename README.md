### Simple web app that displays recipes and related Twitter quotes


1. Create a developer account on Twitter to get the access keys and tokens. [Sign-up here!](https://developer.twitter.com/en/apply-for-access)

   __Important:__ Keep your access keys and tokens safely hidden. Treat them like your passwords.
2. Install flask, tweepy, and dotenv module using the command in your terminal:
```bash
sudo pip install tweepy
sudo pip install flask
sudo pip install python-dotenv
```

3. Clone this repository using the following command in your terminal:
```bash
git clone https://github.com/NJIT-CS490/project1-bcs32
```

4. Do not add your keys in your source code instead create a new root-level file named _tweet.env_ to save your keys. In your _tweet.env_ type:
```text
export KEY='TODO'
export SECRET='TODO'
export TOKEN='TODO'
export SECRET_TOKEN='TODO'
```
 Replace TODO with the appropriate keys. Save the file.
 For additional info check [Tweepy documentation.](http://docs.tweepy.org/en/v3.5.0/auth_tutorial.html)

5. Run your code in your terminal.
```python
python get_tweet.py
```

6. Create your own repository on your Github account. 

 __Important:__ Do not push the _tweet.env_ to Git.
7. Add your source code and .gitignore to your Git.
 ```bash
git remote remove origin 
git remote add origin https://github.com/[your-username]/[your-repo-name]
git commit -am "Add get tweet file with and .gitignore"
git push origin master
 ```
 
8. When prompted, enter your Github credentials. Refresh your Github page and you should be able to see your code here.
 
-------------------
### Troubleshooting some common technical issues

#### Command not found while installing module (flask, tweepy, dotenv) in terminal

pip command will install the packages in Python. When this error (see below) occurs it means that the executable path is not in PATH variable.
```bash
sudo: pip: command not found
```
Go to the root directory and add the executable path to PATH variable.
```bash
cd ~
which pip
```
Copy (ctrl + c) the output of _which pip_ and open a text editor (vim).
```bash
vim .bashrc
```
When the text editor opens, look for 'export PATH=$PATH:$HOME..../bin:', this should be on the first few lines but this might be different in your local machine. At the very end of this line paste (ctrl + v) the output of 'which pip' to the end of PATH, don't add any space. Save and quit the .bashrc by typing ':wq'.
In your terminal, source the .bashrc:
```bash
source ~/.bashrc
```
Try one of the following command again:
```bash
pip install [module]
sudo pip install [module]
```
Resources: [AskUbuntu](https://askubuntu.com/questions/885479/pip-is-apparently-installed-but-not-working)

####  Internal Server Error

When getting the Internal Server Error when opening the html page, the server is preventing the page to load because of incorrect permission. Most common mistakes are in the access keys provided. Check the following:

+ Double check the spelling of __KEY, SECRET, TOKEN, SECRET_TOKEN__ in _tweet.env_ and  this should all match in the _get_tweet.py_
+ Make sure the _tweet.env_ matches the text in .gitignore
+ Check your Twitter keys in your [Twitter account dashboard](https://developer.twitter.com/en/portal/dashboard), copy and paste the keys again, it is possible you copied the wrong key to another variable

------------------------
### Known problems

#### Retweeting the same tweet

When viewing the tweets on the webpage, some users retweet the same tweets hence resulting the same tweets in the page. This can be solved by picking a user who did not retweet the previous tweet.
Tweets has an attribute entities which includes mentions, tagging a user. We can filter the tweets by collecting the username of tweets and get the tweet's mention/s (if any) and compare if it matches to any in the username list.

Resources: [Tweet object documentation] (https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/overview/tweet-object) and [Entities object documentation](https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/overview/entities-object
)
