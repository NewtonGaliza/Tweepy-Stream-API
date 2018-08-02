import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)
        

twitter_stream = Stream(auth, MyStreamListener())
twitter_stream.filter(track=['#python])    
