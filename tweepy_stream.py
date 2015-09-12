# !/usr/bin/env python
# encoding: utf-8

"""
Parse tweets from twitter, use api

@author: Jessie

@email: jessie.JNing@gmail.com
"""

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import pandas as pd
import json


class StdOutListener(StreamListener):

    def __init__(self):
        super(StreamListener, self).__init__()
        self.api = None
        self.tweet_list = []

    def on_data(self, data):

        self.tweet_list.append(data)
        print data
        if len(self.tweet_list)<5:
            return True
        else:
            return False

    '''
    def on_status(self, status):
        #print "screen_name:", status.author.screen_name
        #print "tweet:", status.text

        self.status_list.append(status)

        if len(self.status_list)<5:
            return True
        else:
            return False
    '''



    def on_error(self, status_code):
        print "Got an error with status code:", str(status_code)
        return True

    def on_timeout(self):
        print "Timeout..."
        return True


if __name__=="__main__":

    consumer_key = "4tq3k1I3UaTGPL4MIr7neEbtI"
    consumer_secret = "yvxjOjcR1SIPcT2LOZdapYod1IqK60KGtCL8r91FUxz3K42oH0"
    access_token = "287010952-uE58p1aVSKdOsLSoR4yoXP0FqcrCjh3IO7vyImNd"
    access_token_secret = "MvWlHHbEB3cAXTP5cdCVrjfg6hCXYB0NqvPDjx6OOrW0V"

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    listener = StdOutListener()
    stream = Stream(auth, listener)
    stream.filter(track=['python','javascript', 'ruby'])

    tweets = pd.DataFrame()
    tweets["text"] = map(lambda tweet: json.loads(tweet)["text"], listener.tweet_list)
    tweets["lang"] = map(lambda tweet: json.loads(tweet)["lang"], listener.tweet_list)

    print tweets

