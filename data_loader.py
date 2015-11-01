import codecs
from os import path
import pandas as pd
import pdb
from IPython.core.debugger import Tracer
import logging
import re
import download_tweets as tweetd
__docformat__ = 'restructedtext en'
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

#global constants
home = '/home/arahimi/1semeval2016-task6'
home = '/mnt/ray/1semeval2016-task6'
training_file = path.join(home, 'semeval2016-task6-trainingdata.txt')
dev_file = path.join(home, 'semeval2016-task6-trialdata.txt')
fields = {1:'ID', 2:'Target', 3:'Tweet', 4:'Stance'}
mention_pattern = re.compile('(?<=^|(?<=[^a-zA-Z0-9-_\\.]))@([A-Za-z]+[A-Za-z0-9_]+)')

def init():
	global training_data
	global dev_data
	training_data = pd.read_csv(training_file, header=0, delimiter='\t')
	dev_data = pd.read_csv(dev_file, header=0, delimiter='\t')
	#training_data['Mentions'] = pd.Series([None for i in range(0, len(training_data))], index=training_data.index)

def extract_mentions(data):
	tweets = data['Tweet']
	all_mentions = []
	for id, tweet in tweets.iteritems():
		mentions = [m.lower() for m in mention_pattern.findall(tweet)]
		all_mentions.extend(mentions)
	return set(all_mentions)
if __name__ == '__main__':
	logging.info('initialising...')
	init()
	logging.info('extracting training mentions...')
	train_mentions = extract_mentions(training_data)
	#logging.info('downloading training mentions...')
	#tweetd.download_user_tweets(['@'+m for m in train_mentions], 'train-mention-timelines.txt')
	logging.info('extracting dev mentions...')
	dev_mentions = extract_mentions(dev_data)
	logging.info('downloading dev mentions')
	tweetd.download_user_tweets(['@'+m for m in dev_mentions if m not in train_mentions], 'dev-mention-timelines.txt')
	logging.info('finished dowloading mention tweets.')
	
	
	
	Tracer()()
