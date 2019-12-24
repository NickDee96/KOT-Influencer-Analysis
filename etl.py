import tweepy #https://github.com/tweepy/tweepy
import csv

import json
with open("twitterCreds.json","r") as jFile:
    creds=json.load(jFile)

#Twitter API credentials
consumer_key = creds["consumer_key"]
consumer_secret = creds["consumer_secret"]
access_key = creds["access_key"]
access_secret = creds["access_secret"]
screen_name="migunamiguna"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# initialization of a list to hold all Tweets

all_the_tweets = []

# We will get the tweets with multiple requests of 200 tweets each

new_tweets = api.user_timeline(screen_name=screen_name, count=200)
all_the_tweets.extend(new_tweets)

# save id of 1 less than the oldest tweet

oldest_tweet = all_the_tweets[-1].id - 1

# grabbing tweets till none are left

while len(new_tweets) > 0:
    # The max_id param will be used subsequently to prevent duplicates
    new_tweets = api.user_timeline(screen_name=screen_name,
    count=200, max_id=oldest_tweet)
    # save most recent tweets

    all_the_tweets.extend(new_tweets)

    # id is updated to oldest tweet - 1 to keep track

    oldest_tweet = all_the_tweets[-1].id - 1
    print ('...%s tweets have been downloaded so far' % len(all_the_tweets))

# transforming the tweets into a 2D array that will be used to populate the csv

outtweets = [[tweet._json["id_str"],tweet._json["created_at"],tweet._json["text"],tweet._json["geo"],tweet._json["coordinates"],tweet._json["retweet_count"],tweet._json["favorite_count"]] for tweet in all_the_tweets]



# writing to the csv file

with open(screen_name + '_tweets.csv', 'w', encoding='utf8') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'created_at', 'text','geo','coordinates','retweet_count','favorite_count'])
    writer.writerows(outtweets)

