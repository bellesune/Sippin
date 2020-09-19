### Simple web app that displays recipes and related Twitter quotes

##### Module 1 - Get tweets using a specific keyword

1. Install tweepy module using the command in your terminal
```bash
  pip install tweepy
```

2. Create a developer account on Twitter to get the access keys and tokens. [Sign-up here](https://developer.twitter.com/en/apply-for-access)
   __Note:__ Keep your access keys and tokens safely hidden. Treat them like your passwords.

3. Do not add your keys in your source code instead create a new file named _keys.env_ to save your keys. In your _keys.env_ type:
```bash
  export KEY='TODO'
  export SECRET_KEY='TODO'
  export TOKEN='TODO'
  export SECRET_TOKEN='TODO'
```
  Replace TODO with the appropriate keys. Save the file and source it.
  ```bash
    source keys.env
  ```
  For additional info: Check Tweepy documentation. [Click here](http://docs.tweepy.org/en/v3.5.0/auth_tutorial.html)
 
 __Important:__ Do not push the _keys.env_ to Git instead you will hide it in .gitignore
 4. In your terminal type the following commands, this will hide the contents of _keys.env_
 ```bash
  $ echo "keys.env" >> .gitignore
  $ git init
  $ git add .gitignore
 ```
 
 5. Add your source code and push the python file and .gitignore to Git.
 ```bash
  $ git add filename.py
  $ git commit -m "Add source code and.gitignore"
 ```
 
 6. Open your Github account and create a new repository. Copy and paste the commands on __…or push an existing repository from the command line__ to your terminal.
 7. When prompted, enter your Github credentials. Refresh your Github page and you should be able to see your code here.
 
 
 
 
