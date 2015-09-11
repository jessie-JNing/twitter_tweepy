#!/usr/bin/env python
# encoding: utf-8

"""
Parse tweets from twitter, start up

@author: Jessie

@email: jessie.JNing@gmail.com
"""

import tweepy

def home_timeline(api):
    public_tweens = api.home_timeline()
    for tweet in public_tweens:
        print tweet.text

def cursor(api):

    user = tweepy.Cursor(api.user_timeline, id="twitter").items(20)




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

    # print user methods
    cursor(tp_api)

    for md in dir(tp_api):
        print md




