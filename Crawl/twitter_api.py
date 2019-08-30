# import twitter
# api = twitter.Api(consumer_key='consumer_key',
#                       consumer_secret='consumer_secret',
#                       access_token_key='access_token',
#                       access_token_secret='access_token_secret')
# print(api.VerifyCredentials())
#
#
# statuses = api.GetUserTimeline(screen_name="realDonaldTrump", count=10)

# # Iterate through them and analyse them
# for status in statuses:
#   anaylse_tweet(html.unescape(status.full_text), word_weights)
# #
# import tweepy
# import json
#
# consumer_key = "你的参数"
# consumer_secret = "你的参数"
# access_token = "你的参数"
# access_token_secret = "你的参数"
#
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

import requests
import save_file
import pandas as pd
import csv_to_xls
def get_twitter(url ='http://www.trumptwitterarchive.com/data/realdonaldtrump/2018.json'):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/62.0'}
    res = requests.get(url, headers=headers)
    data = res.json()
    #datalist = [[d['text'], d['created_at'], d['retweet_count'], d['favorite_count'], d['is_retweet']] for d in data]
    text = [d['text'] for d in data]
    return text


# url = 'http://www.trumptwitterarchive.com/data/realdonaldtrump/2018.json'
# data = get_twitter(url)
# print(len(data),data[0])

# for d in data:
#     if 'china' or 'China' or 'trade' in d['text']:
#         print(d)
# #         dt = [d['text'], d['created_at'], d['retweet_count'], d['favorite_count'], d['is_retweet']]
# #         save_file.save_to_csv('trump-china',dt)
# csv_to_xls('')