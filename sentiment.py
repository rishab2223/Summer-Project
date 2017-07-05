
import sys
import os
from pymongo import MongoClient
import re
from nltk.corpus import twitter_samples
from nltk.corpus import stopwords
import string
import nltk
from pymongo import MongoClient
from textblob import TextBlob

client = MongoClient('localhost', 27017)
db = client['twitterdb']
collection = db['twitter_collection']
cursor = collection.find({})



def get_tweet_sentiment( tweet):

	analysis = TextBlob(tweet)
	a = analysis.sentiment.polarity
	if a > 0:
		print(a)
		return 'positive'
	elif a == 0:
		print(a)
		return 'neutral'
	else:
		return 'negative'
		print(a)


for row in cursor:
	stri = get_tweet_sentiment(row['text'])
	print(stri)


# pos_tweets = [	('I love this car', 'positive'),
# 				('This view is amazing', 'positive'),
# 				('I feel great this morning', 'positive'),
# 				('I am so excited about the concert', 'positive'),
# 				('He is my best friend', 'positive')]

# neg_tweets = [	('I do not like this car', 'negative'),
# 				('This view is horrible', 'negative'),
# 				('I feel tired this morning', 'negative'),
# 				('I am not looking forward to the concert', 'negative'),
# 				('He is my enemy', 'negative')] 



# test_tweets = [

# 				(['feel', 'happy', 'this', 'morning'], 'positive'),
# 				(['larry', 'friend'], 'positive'),
# 				(['not', 'like', 'that', 'man'], 'negative'),
# 				(['house', 'not', 'great'], 'negative'),
# 				(['your', 'song', 'annoying'], 'negative')]

# tweets = []
# for (words, sentiment) in pos_tweets + neg_tweets:
# 	words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
# 	tweets.append((words_filtered, sentiment))


# def get_words_in_tweets(tweets):
# 	all_words = []
# 	for (words, sentiment) in tweets:
# 		all_words.extend(words)
# 	return all_words

# def get_word_features(wordlist):
# 	freq = nltk.FreqDist(wordlist)
# 	word_features = freq.keys()
# 	return word_features

# def extract_features(document):
# 	document_words = set(document)
# 	features = {}
# 	for word in word_features:
# 		features['contains(%s)' % word] = (word in document_words)
# 	return features

# training_set = nltk.classify.apply_features(extract_features,tweets)

# def train(labeled_featuresets, estimator=ELEProbDist):
# 	label_probdist = estimator(label_freqdist)
# 	feature_probdist = {}
# 	return NaiveBayesClassifier(label_probdist, feature_probdist)


# word_features = get_word_features(get_words_in_tweets(tweets))	

# classifier = nltk.NaiveBayesClassifier.train(training_set)

# print (label_probdist.prob('negative'))

