from twython import Twython, TwythonError
execfile("keys")


twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)
twitter.verify_credentials()

#Search for something and then print it
results = twitter.search(q="#Bhasin", count=20)
all_tweets = results['statuses']

for i in all_tweets:
    print (i['text'])

#print timeline and what people device used to tweet
#timeline = twitter.get_home_timeline()
#for i in timeline:
#    print i['source']
