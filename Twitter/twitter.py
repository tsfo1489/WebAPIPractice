from requests.sessions import session
import tweepy
from tweepy import api
import apikey
import datetime

def time_format(date : datetime.datetime) :
    return date.strftime('%Y-%m-%d')

auth = tweepy.OAuthHandler(apikey.consumer_key, apikey.consumer_secret)

auth.set_access_token(apikey.access_token_key, apikey.access_token_secret)

api = tweepy.API(auth)
today_date = datetime.datetime.now()

for i in range(7) :
    date = time_format(today_date - datetime.timedelta(days=i))
    results = api.search_tweets('점심', lang='ko', count=100, until=date)
    print(date, len(results))
    if len(results) != 0 :
        print(results[0].text)