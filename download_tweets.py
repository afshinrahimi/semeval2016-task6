'''
Created on 11 Sep 2014

@author: af
'''
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import codecs
import json
import sys
import tweepy
import pickle
import logging
__docformat__ = 'restructedtext en'
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)




def download_user_tweets(user_ids, output_file):
    # Go to http://dev.twitter.com and create an app.
    # The consumer key and secret will be generated for you after
    consumer_key = 'COVV87zJN2wHRfAz7zB5p2QPQ'
    consumer_secret = 'HhNmLOsIui0rG04XltDSHdmEBNf9IAtkZeW17U7pFYAuKf8qiv'
    
    # After the step above, you will be redirected to your app's page.
    # Create an access token under the the "Your access token" section
    access_token = '2205031009-a7FMWRzzTi5wooSMFkYUqyiq1aGREBSMCyBX2vw'
    access_token_secret = 'TfPQ5V8X9BOwjWQU7UBTJHTR8kYJzyhM1em8I4YGIcZxh'    
    
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    tfile = codecs.open(output_file, 'a+', 'utf-8')
    api = tweepy.API(auth, wait_on_rate_limit=True)
    
    
    for u_id in user_ids:
        try:
            timeline_statuses = api.user_timeline(u_id)
        except:
            logging.info('Unexpected Error' + str(sys.exc_info()[0]))
            continue
        for s in timeline_statuses:
            json.dump(s._json, tfile)
            tfile.write('\n')
            tfile.flush()  

if __name__ == '__main__':
    pass
