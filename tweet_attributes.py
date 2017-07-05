import json
import sys
import os
from pymongo import MongoClient
import re
from nltk.corpus import twitter_samples
from nltk.corpus import stopwords
import string
import nltk
import emoticons


client = MongoClient('localhost', 27017)
db = client['twitterdb']
collection = db['twitter_collection']
cursor = collection.find({})





for row in cursor:

# 	1) Calculate tweet length
	# l = len(row['text'])

# 	2) Calculate number of words ,hashtag,url,mentions

	# emoticons_str = r"""
	# 			(?:
	# 							[:=;] # Eyes
	# 							[oO\-]? # Nose (optional)
	# 							[D\)\]\(\]/\\OpP] # Mouth
	# 			)"""
	# regex_str = [
	# 				emoticons_str,
	# 				r'<[^>]+>', # HTML tags
	# 				r'(?:@[\w_]+)', # @-mentions
	# 				r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
	# 				r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
		
	# 				r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
	# 				r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
	# 				r'(?:[\w_]+)', # other words
	# 				r'(?:\S)' # anything else
	# ]
			
	# tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
	# emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
		
	# def tokenize(s):
	# 	return tokens_re.findall(s)
		
	# def preprocess(s, lowercase=False):
	# 	tokens = tokenize(s)
	# 	if lowercase:
	# 		tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
	# 	return tokens

	# punctuation = list(string.punctuation)
	# stop = stopwords.words('english') + punctuation
	# list1=[] 
	# list1 = [term for term in preprocess(row['text']) if term not in stop]
	# list2 =[]
	# list2 = preprocess(row['text'])

	# count_mention = 0
	# count_hashtag = 0
	# count_url = 0
	# count_word = 0

	# list_mention=[]
	# list_hashtag=[]
	# list_url=[]
	# list_word=[]

	# for a in list1:
	# 	if a[0] == "@":
	# 		count_mention += 1
	# 		list_mention.append(a)
	# 	elif a[0] == "#":
	# 		count_hashtag += 1
	# 		list_hashtag.append(a)
	# 	elif a[0] =="h" and a[1] == "t"	and a[2] == "t"	and a[3] == "p"	and a[4] == "s"	:
	# 		count_url += 1
	# 		list_url.append(a)	
	# 	else :
	# 		count_word +=1
	# 		list_word.append(a)

	# print(row['text'])
	# print("mention", count_mention, list_mention)
	# print("hashtag",count_hashtag, list_hashtag)
	# print("url",count_url,list_url)
	# print("word",count_word,list_word)


#	4) no of question and exclamanation marks

	# print(preprocess(row['text']))
	# contains_ques = False
	# count_ques = 0
	# contains_ex = False
	# count_ex = 0
	# for a in list2:
	# 	if a[0] == "?":
	# 		contains_ques = True
	# 		count_ques +=1

	# 	elif a[0] == "!":
	# 		contains_ex= True
	# 		count_ex +=1
	# print(contains_ques,"ques")
	# print(count_ques,"ques")
	# print(contains_ex,"ex")
	# print(count_ex,"ex")	

#	5)pronoun count
	# print(row['text'])
	# count_pronoun =0
	# pos = nltk.pos_tag(preprocess(row['text']))
	# for a in pos:
	# 	if a[1] == "PRP" or a[1] == "PRP$" or a[1] == "WP":
	# 		count_pronoun+= 1
	# 		print(a[1])
	# print(count_pronoun)		

	

#	6)emoticon count	
	count_emojis = 0
	list_emojis= []
	happy_emojis = []
	sad_emojis  = []
	list_emojis = emoticons.find_emoticons(''.join(list_word))
	print(row['text'])
	print(list_emojis,len(list_emojis))
	for a in list_emojis:
		if len(list_emojis) == 0:
			print("no emojis")
		elif len(list_emojis) != 0:
			emojis = emoticons.analyze_tweet(''.join(a))
			print(emojis)
			if emojis == "HAPPY" or emojis =="WINK" or emojis == "TONGUE":
				happy_emojis.append(''.join(a))
			elif emojis == "SAD":
				sad_emojis.append(''.join(a))

	print(len(happy_emojis),happy_emojis)
	print(len(sad_emojis), sad_emojis)

	count_happy = len(happy_emojis)
	count_sad = len(sad_emojis)

 
#	7) no of upper case and lower case letters
	# count_uppercase = 0
	# count_lowercase = 0
	# for word in list_word:
	# 	for c in word:
	# 		if c.isupper():
	# 			count_uppercase += 1
	# 		elif c.islower():
	# 			count_lowercase += 1
	# 		else:
	# 			pass
	# print ("No. of Upper case characters : ", count_uppercase)
	# print ("No. of Lower case Characters : ", count_lowercase)

#	8) sentiment analysis	
	


# 	#Update features in MongoDB
	# collection.update_one({'_id': row['_id']},{
	# 	'$set': { 'number of mention': count_mention, 'number of hashtag' : count_hashtag,'no of url' :count_url,'number of word':count_word}
	# 	}, upsert=False)