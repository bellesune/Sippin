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

##### Error in installing module (flask, tweepy, dotenv)
Try one of the following command:
```bash
sudo pip3 install [module]
pip install [module]
pip3 install [module]
```

#####  Cannot see the tweet output:
+ Double check the spelling of __KEY, SECRET, TOKEN, SECRET_TOKEN__ in _tweet.env_ and  this should all match in the _get_tweet.py_
+ Make sure the _tweet.env_ matches the text in .gitignore
+ Check your Twitter keys in your Twitter account, copy and paste the keys again, it is possible you copied the wrong key to another variable
