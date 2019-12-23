import tweepy #https://github.com/tweepy/tweepy
import csv

#Twitter API credentials
consumer_key = "CEiEjqTd982VZd9VVv2YT2BAA"
consumer_secret = "RkPqz03jI3KjpNlZ7uCqugf7JCdbqm2BB2ZqK5It4NgUoHrRBI"
access_key = "2268398615-r29heFTnTs5EFOmcnkvnarE8keDrWd5S913VPLV"
access_secret = "4Oynqk6h2nKIxnS9dlFUK2lDPCLwfKN0UK2NlHKUu6Bpn"
screen_name="CrazyNairobian"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# initialization of a list to hold all Tweets

all_the_tweets = []

# We will get the tweets with multiple requests of 200 tweets each

new_tweets = api.user_timeline(screen_name=screen_name, count=200)

# saving the most recent tweets

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

outtweets = [[tweet.id_str, tweet.created_at,tweet.text.encode('utf-8')] for tweet in all_the_tweets]

# writing to the csv file

with open(screen_name + '_tweets.csv', 'w', encoding='utf8') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'created_at', 'text'])
    writer.writerows(outtweets)

