import tweepy
import os

auth = tweepy.OAuthHandler(os.environ["FOOD_BOT_CK"], os.environ["FOOD_BOT_CS"])
auth.set_access_token(os.environ["FOOD_BOT_TOKEN"], os.environ["FOOD_BOT_TOKEN_S"])

api = tweepy.API(auth)

api.update_status('Updating using OAuth authentication via Tweepy!')

