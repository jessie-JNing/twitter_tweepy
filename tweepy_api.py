#!/usr/bin/env python
# encoding: utf-8

"""
Parse tweets from twitter, use api

@author: Jessie

@email: jessie.JNing@gmail.com
"""

import tweepy

def home_timeline(api):
    public_tweens = api.home_timeline()
    for tweet in public_tweens:
        print tweet.text

def get_me(api):
    user = api.me()
    print "Name:", user.name
    print "Loaction:", user.location
    print "Friends:", user.friends_count



if __name__=="__main__":
    consumer_key = "4tq3k1I3UaTGPL4MIr7neEbtI"
    consumer_secret = "yvxjOjcR1SIPcT2LOZdapYod1IqK60KGtCL8r91FUxz3K42oH0"
    access_token = "287010952-uE58p1aVSKdOsLSoR4yoXP0FqcrCjh3IO7vyImNd"
    access_token_secret = "MvWlHHbEB3cAXTP5cdCVrjfg6hCXYB0NqvPDjx6OOrW0V"

    # initialize and create tweepy object
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    tp_api = tweepy.API(auth)

    # download your home timeline tweets and print each one of their texts to the console
    home_timeline(tp_api)

    # the user whole authentication keys were used
    get_me(tp_api)




