import json
import tweepy
import sys
import os
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client['twitterdb']
collection_keys = db['keys']

keys = []
cursor = collection_keys.find({})
for row in cursor:
	keys.append(row)

key_num = 1
flag = False
auth = tweepy.AppAuthHandler(keys[key_num]['ckey'], keys[key_num]['consumer_secret'])
# auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)

searchQuery = ('#DonaldTrump')
collection = db['twitter_collection']
maxTweets = 50 
tweetsPerQry = 10

sinceId = None
max_id = -1L

tweetCount = 0
print("Downloading max {0} tweets".format(maxTweets))
while tweetCount < maxTweets:
	print("inside while loop")
	try:
		# print(max_id)
		if (max_id <= 0):
			if (not sinceId):
				new_tweets = api.search(q=searchQuery, count=tweetsPerQry)
				print(1)
			else:
				new_tweets = api.search(q=searchQuery, count=tweetsPerQry, since_id=sinceId)
				print(2)
		else:
			if (not sinceId):
				new_tweets = api.search(q=searchQuery, count=tweetsPerQry, max_id=str(max_id - 1))
				print(3)
			else:
				new_tweets = api.search(q=searchQuery, count=tweetsPerQry, max_id=str(max_id - 1), since_id=sinceId)
				print(4)
		print(len(new_tweets))
		if len(new_tweets) == 0:
			# if flag == True:
			# 	# code to sleep
			# 	continue
			if key_num < len(keys) - 1:
				# flag = False
				key_num += 1
			else:
				# flag = True
				key_num = 0
			auth = tweepy.AppAuthHandler(keys[key_num]['ckey'], keys[key_num]['consumer_secret'])
			api = tweepy.API(auth)
			print("Keys changed!", key_num)
			continue
		for tweet in new_tweets:
			collection.insert(tweet._json)
		tweetCount += len(new_tweets)
		print("Downloaded {0} tweets".format(tweetCount))
		max_id = new_tweets[-1].id
		print max_id, "max"
	except tweepy.TweepError as e:
		print("some error : " + str(e))
		break

print ("Downloaded {0} tweets total.".format(tweetCount))


# for status in tweepy.Cursor(api.user_timeline, screen_name='#DonaldTrump').items(20):

# 	collection = db['twitter_collection']
# 	print("collecting data")
# 	collection.insert(status._json)