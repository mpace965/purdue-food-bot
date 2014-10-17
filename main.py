import tweepy
import json
import os

class StdOutListener(tweepy.StreamListener):
  def __init__(self, api):
    self.api = api
    super(tweepy.StreamListener, self).__init__()
  
  def on_data(self, data):
    json_data = json.loads(data)
    print '@%s' % json_data['user']['screen_name']
    return True

  def on_error(self, status):
    print status

auth = tweepy.OAuthHandler(os.environ["FOOD_BOT_CK"], os.environ["FOOD_BOT_CS"])
auth.set_access_token(os.environ["FOOD_BOT_TOKEN"], os.environ["FOOD_BOT_TOKEN_S"])

api = tweepy.API(auth)

listener = StdOutListener(api)
stream = tweepy.Stream(auth, listener)
stream.filter(track=['@PurdueFoodBot'])

