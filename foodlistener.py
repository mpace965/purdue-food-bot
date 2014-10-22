
import datetime
import json
import urllib2
import xml.etree.ElementTree as ET

import tweepy

class FoodListener(tweepy.StreamListener):

    EARHART = 1
    FORD = 2
    HILLENBRAND = 3
    WILEY = 4
    WINDSOR = 5
    
    court = 0

    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()
  
    def on_data(self, data):
        json_data = json.loads(data)

        find_court(json_data['text'])
        response = construct_response(json_data)
        api.update_status(response)

        return True
    
    def find_court(self, tweet):
        tweet_lower = tweet.lower()

        if 'earhart' in tweet_lower:
            self.court = self.EARHART
        elif 'ford' in tweet_lower:
            self.court = self.FORD
        elif 'hillenbrand' in tweet_lower:
            self.court = self.HILLENBRAND
        elif 'wiley' in tweet_lower:
            self.court = self.WILEY
        elif 'windsor' in tweet_lower:
            self.court = self.WINDSOR
        else:
            self.court = -1
    
    def construct_response(self, json_data):
        if self.court > 0:
            return self.select_random()
        else:
            return '@%s, I could not find a dining court in your tweet.' % json_data['user']['screen_name']

    def select_random(self):
        today = datetime.date.today()
        url = 'http://api.hfs.purdue.edu/menus/v1/locations/%s/%d-%d-%d' % (self.court_to_text(), today.month, today.day, today.year)
        xml = urllib2.urlopen(url)
        tree = ET.parse(xml)
        """
        root = tree.getroot()
        
        for child in root:
                print child.tag, child.attrib
        """
    def court_to_text(self):
        if self.court == self.EARHART:
            return 'Earhart'
        elif self.court == self.FORD:
            return 'Ford'
        elif self.court == self.HILLENBRAND:
            return 'Hillenbrand'
        elif self.court == self.WILEY:
            return 'Wiley'
        elif self.court == self.WINDSOR:
            return 'Windsor'

