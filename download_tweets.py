'''
Created on 11 Sep 2014

@author: af
'''
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import codecs
import json
from os import path
import sys
import tweepy
import pickle
from IPython.core.debugger import Tracer
import logging
from tweepy.api import API
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

def download_tweets(tweets_ids, filename):
    # Go to http://dev.twitter.com and create an app.
    # The consumer key and secret will be generated for you after
    consumer_key = 'COVV87zJN2wHRfAz7zB5p2QPQ'
    consumer_secret = 'HhNmLOsIui0rG04XltDSHdmEBNf9IAtkZeW17U7pFYAuKf8qiv'
    consumer_key = 'XtggSrSiLNvG3IlY95mRDCktI'
    consumer_secret = 'd5EfMArRUfdOg7nnAKpfG49N5Va0QMfM2Rgy8xec59lBBeod3K'    
    # After the step above, you will be redirected to your app's page.
    # Create an access token under the the "Your access token" section
    access_token = '2205031009-a7FMWRzzTi5wooSMFkYUqyiq1aGREBSMCyBX2vw'
    access_token_secret = 'TfPQ5V8X9BOwjWQU7UBTJHTR8kYJzyhM1em8I4YGIcZxh'    
    access_token = '2205031009-8kQqA0cmi24mVoOLpIcxc8YtkG6GUYXtOZJfMN9'
    access_token_secret = 'bk8WuRZF7GwzjhFkYAxxMcHc1dlyA7cf27oI1EEKCMHWS'    
    
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    tfile = codecs.open(filename, 'a+', 'utf-8')
    api = tweepy.API(auth, wait_on_rate_limit=True)
    i = 0 
    for tweet_id in tweets_ids:
        i+= 1
        if i % 1000 == 0:
            print 'downloading tweet ', i
        try:
            status = api.get_status(tweet_id)
        except:
            continue
        json.dump(status._json, tfile)
        tfile.write('\n')
        tfile.flush()
    tfile.close()
    '''
    tweets_ids = list(tweets_ids)
    chunks=[tweets_ids[x:x+100] for x in xrange(0, len(tweets_ids), 100)]
    i = 0
    for chunk in chunks:
        statuses = api.statuses_lookup(chunk, include_entities=True)
        for status in statuses:
            i += 1
            if i % 1000 == 0:
                print 'downloaded tweets: ', i
            if status:
                json.dump(status._json, tfile)
                tfile.write('\n')
                tfile.flush()
    tfile.close()
    '''
def download_trum_tweets():
    tweet_id_file = './semeval2016-task6-domaincorpus/Donald_Trump.txt'
    tweet_ids = set()
    with codecs.open(tweet_id_file, 'r', encoding='utf-8') as inf:
        for line in inf:
            line = line.strip()
            tweet_ids.add(line)
    download_tweets(tweet_ids, './semeval2016-task6-domaincorpus/downloaded_Donald_Trump.txt.json')

def dowanload_timeline_of_ids(userids=None, inputfilename=None, outputfilename='timeline.txt'):
    print 'downloading time line of celebrities'
    print 'input file : ' + inputfilename
    print 'output file : ' + outputfilename
    already_downloaded = set()
    if path.exists(outputfilename):
        with codecs.open(outputfilename, 'r', encoding='utf-8') as inf:
            for line in inf:
                obj = json.loads(line)
                if 'user' in obj:
                    if 'id_str' in obj['user']:
                        already_downloaded.add(obj['user']['id_str'])
    print 'already downloaded: ' , len(already_downloaded)
    lines = []
    if not userids and inputfilename:
        with codecs.open(inputfilename, 'r', encoding='utf-8') as inf:
            lines = inf.readlines()
            lines = [l.strip() for l in lines]
            #choose second column tab separated
            userids = [l.split('\t')[0] for l in lines]
    print 'number of celebrities: ', len(userids)
    userids = [l for l in userids if l not in already_downloaded]
    print 'celebrity timelines to download: ' , len(userids)
    consumer_key = 'COVV87zJN2wHRfAz7zB5p2QPQ'
    consumer_secret = 'HhNmLOsIui0rG04XltDSHdmEBNf9IAtkZeW17U7pFYAuKf8qiv'
    consumer_key = 'XtggSrSiLNvG3IlY95mRDCktI'
    consumer_secret = 'd5EfMArRUfdOg7nnAKpfG49N5Va0QMfM2Rgy8xec59lBBeod3K'    
    # After the step above, you will be redirected to your app's page.
    # Create an access token under the the "Your access token" section
    access_token = '2205031009-a7FMWRzzTi5wooSMFkYUqyiq1aGREBSMCyBX2vw'
    access_token_secret = 'TfPQ5V8X9BOwjWQU7UBTJHTR8kYJzyhM1em8I4YGIcZxh'    
    access_token = '2205031009-8kQqA0cmi24mVoOLpIcxc8YtkG6GUYXtOZJfMN9'
    access_token_secret = 'bk8WuRZF7GwzjhFkYAxxMcHc1dlyA7cf27oI1EEKCMHWS'    
    
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    tfile = codecs.open(outputfilename, 'a+', 'utf-8')
    i = 0
    for u_id in userids:   
        i += 1
        if i % 100 == 0:
            print 'record ', i
        try:
            timeline_statuses = api.user_timeline(u_id)
        except:
            logging.info('Unexpected Error' + str(sys.exc_info()[0]))
            continue
        for s in timeline_statuses:
            json.dump(s._json, tfile)
            tfile.write('\n')
            tfile.flush() 
              
            
def download_user_friends_info(list_of_users, inputfilename=None, outputfilename='533_followers.txt'):
    consumer_key = 'COVV87zJN2wHRfAz7zB5p2QPQ'
    consumer_secret = 'HhNmLOsIui0rG04XltDSHdmEBNf9IAtkZeW17U7pFYAuKf8qiv'
    
    # After the step above, you will be redirected to your app's page.
    # Create an access token under the the "Your access token" section
    access_token = '2205031009-a7FMWRzzTi5wooSMFkYUqyiq1aGREBSMCyBX2vw'
    access_token_secret = 'TfPQ5V8X9BOwjWQU7UBTJHTR8kYJzyhM1em8I4YGIcZxh'    
    
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    tfile = codecs.open(outputfilename, 'a+', 'utf-8')
    
    already_downloaded = set()
    if path.exists(outputfilename):
        with codecs.open(outputfilename, 'r', encoding='utf-8') as inf:
            for line in inf:
                userid = line.split('\t')[0]
                already_downloaded.add(userid)
    print "already downloaded follows: " , len(already_downloaded)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    if not list_of_users and inputfilename:
        with codecs.open(inputfilename, 'r', encoding='utf-8') as inf:
            lines = inf.readlines()
            list_of_users = [l.split('\t')[1].strip() for l in lines]
            list_of_users = list(set(list_of_users))
    
    print 'the number of users is: ' , len(list_of_users)
    list_of_users = [u for u in list_of_users if u not in already_downloaded]
    print 'users to download their followers: ', len(list_of_users)
    i = 0
    for userid in list_of_users:
        try:
            ids = api.friends_ids(userid)
        except:
            continue

        i += 1
        if i % 100 == 0:
            print 'downloaded till now: ', i
        for id in ids:
            tfile.write(str(userid) + '\t' + str(id) + '\n')
            tfile.flush()
    tfile.close()
        
    
    
if __name__ == '__main__':
    #download_trum_tweets()
    dowanload_timeline_of_ids(inputfilename='533_retweeters.txt', outputfilename='timeline-retweeters.txt')
    #download_user_friends_info(list_of_users=None, inputfilename='533_retweeters.txt')
