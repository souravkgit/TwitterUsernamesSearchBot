# What is this repo about?
This is a [telegram bot](https://t.me/TwitterUsernameSearchBot) written in python for Searching availability of any username on twitter and it's deployed on [Heroku](https://heroku.com).

# Inspiration 
This project is heavily inspired from [@goyalcompany's](https://t.me/goyalcompany) request.

# Features supported:
- Can search Multiple usernames at once
- Can convert any username into twitter link
- Can Stop any ongoing function on user request
- More features in future

# How to deploy?
Deploying is pretty much straight forward and is divided into several steps as follows:
## Installing requirements

- Clone this repo:
```
git clone https://github.com/souravkgit/TwitterUsernamesSearchBot/
```

- Install requirements
For Debian based distros
```
sudo apt install python3
```
or

Install python from [Here](https://www.python.org/)
- Install dependencies for running setup scripts:
```shell script
pip3 install -r requirements.txt
```
## Procfile
- If you want to deploy your bot on Heroku then you can create this Procfile  , You just have to change File name with your file name like
```
worker: python3 bot.py -----> worker: python3 <your file name>.py
```

## Setting up config file
```
cp config.ini
```
Fill up all the fields given below . Meaning of each fields are discussed below:
- **Token** : The telegram bot token that you get from @BotFather
- **consumer_key** : Twitter Developer Account consumer key , For this you have to create a Twitter developer account.
- **consumer_secret** : Twitter Developer Account consumer key secret , For this you have to create a Twitter developer account.
- **access_token** : Twitter Developer Account app access token , For this you have to create a Twitter developer account.  
- **access_token_secret** : Twitter Developer Account app access token secret , For this you have to create a Twitter developer account.

## Getting Twitter Developer Auth credentials

- Visit the [Twitter Developer Platform](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api)
- Sign up for a developer account by filling just few basic details.
- Agree for the Developer agreement & policy and Submit and then confirm your mail.
- After verifying mail create an app by putting name and hit get keys.
- Save your keys safely (if lost you have to generate new ones).
- Then come to your profile dashboard and then go on your project/app.
- Then go on keys and tokens and then generate **Access Token and Secret**.
- Then it will pop-up all of your API keys and secrets , save them all carefully.
- May be you need to apply for elevated access for this code so if that's the case then follow these steps .
- [Go here](https://developer.twitter.com/en/portal/products/elevated) and apply for Elevated access.
- Fill few details and it's done.
- It will take few minutes to verify and then it's done ,You can use it perfectly.
- Done!!

## Deploying

- Just upload or push your code to a github repository
- Connect your github to your heroku and deploy that repo to your heroku app
```

OR
```
- Just go [Here](https://www.freecodecamp.org/news/how-to-deploy-a-nodejs-app-to-heroku-from-github-without-installing-heroku-on-your-machine-433bec770efe/) and Read from **Step2**.


- Congrats it's done your own bot is now working perfectly fine.

## Thanks for reading this.