import os

import tweepy

from foodlistener import FoodListener

auth = tweepy.OAuthHandler(os.environ['FOOD_BOT_C'], os.environ['FOOD_BOT_CS'])
auth.set_access_token(os.environ['FOOD_BOT_TOKEN'], os.environ['FOOD_BOT_TOKEN_S'])

api = tweepy.API(auth)

listener = FoodListener(api)
listener.court = 1
listener.select_random()

"""
stream = tweepy.Stream(auth, listener)
stream.filter(track=['@PurdueFoodBot'])
"""

