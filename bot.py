#! /usr/bin/python3
# Twitter username bot , coded by @souravkkk or Sourav Goyal


# Import these libraries from python

import telebot
import time
import tweepy as tw
import configparser

# Reading our config file for credentials.
config = configparser.ConfigParser()
config.read('config.ini')

# Defining keys using credentials from config file.
TOKEN = config['Telegram']['Token']
consumer_key = config['Twitter']['consumer_key']
consumer_secret = config['Twitter']['consumer_secret']
access_token = config['Twitter']['access_token']
access_token_secret = config['Twitter']['access_token_secret']

# Defining basic details that will be used in code. 
RUNI = []
bot = telebot.TeleBot(TOKEN)

# Defining function to convert user text into args
def getargs(text):
    _args = text.split()[1:]
    return _args

# Code for bot commands start from here ....

# First command for /start button 
@bot.message_handler(commands=["start"])
def sayhello(message):
    RUNI.clear(-1)
    bot.send_message(message.chat.id,"Hello Hooman , Welcome to my Bot\n Use Given Commands to explore me!")

# Second command for /help button
@bot.message_handler(commands=["help"])
def sayhelp(message):
    bot.send_message(message.chat.id,"What you find tough so you seek help hooman??")

# Third command for /stop button ---> Helps to stop any ongoing function
@bot.message_handler(commands=["st","stop"])
def stop(message):
    RUNI.pop()
    RUNI.append("stop")

# Fourth command for /link button ---> Helps to create twitter link for any twitter username
@bot.message_handler(commands=["l","link"])
def nametolink(message):
    RUNI.append("run")
    args = getargs(message.text)
    text = " ".join(args[0:])
    if len(text)>300:
        bot.send_message(message.chat.id,"Whoaa kid! Have some patience and give a smaller message to convert!")
        return
    text = list(text.split())
    if (len(text)==0):
        bot.send_message(message.chat.id,"Whoaa! kid atleast give one username to change!!")
        return 
    for each in text:
        if (RUNI[-1] == "stop"):
            bot.send_message(message.chat.id,"Okay Sire!! Stopping bot as you said!!")
            RUNI.pop(-1)
            time.sleep(4)
            break 
        if (each[0]=='@'):
            each = "https://twitter.com/" + each[1:]
        elif(each[0:5]=="https"):
            bot.send_message(message.chat.id,"Whoaa! Hooman this is already a link!")
        else:
            each = "https://twitter.com/" + each
        try:
            bot.send_message(message.chat.id,each)
        except Exception as e:
            bot.send_message(message.chat.id,f"What u Wanna find Nigga?? .... {e}")

# Fifth command for /search button ---> Helps to search for availability of any username on twitter
@bot.message_handler(commands=["s","search"])
def namesearch(message):
    RUNI.append("run")
    args = getargs(message.text)
    text = " ".join(args[0:])
    if len(text)>800:
        bot.send_message(message.chat.id,"Whoaa kid! Have some patience and give some less usernames to search!!")
        return
    text = list(text.split())
    remain = []
    if (len(text)==0):
        bot.send_message(message.chat.id,"Whoaa! kid atleast give one username to search!!")
        return
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)
    for each in text:
        if (RUNI[-1] == "stop"):
            bot.send_message(message.chat.id,"Okay Sire!! Stopping bot as you said!!")
            RUNI.pop(-1)
            time.sleep(2)
            break
        try:
            user = api.get_user(screen_name=each)
            printi = f"👤Username : {each}\n\n✅Status : Exist"
            bot.send_message(message.chat.id,printi)
        except:
            printi = f"👤Username : {each}\n\n❌Status : Doesn't Exist"
            remain.append(each)
            bot.send_message(message.chat.id,printi)
    if (len(remain)==0):
        bot.send_message(message.chat.id,"This Bot is created by @souravkkk")
        return 
    bot.send_message(message.chat.id,"The usernames Which Don't exist are :\n")
    for each in remain:
        bot.send_message(message.chat.id,each)
    bot.send_message(message.chat.id,"This Bot is created by @souravkkk")

# For polling of bot.
while True:
    try:
        bot.polling()
    except:
        time.sleep(5)
