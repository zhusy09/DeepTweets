import os
import sys
if sys.version_info[0] < 3:
    raise Exception("Python 2.x is not supported. Please upgrade to 3.x")

sys.path.append(os.path.join(os.path.dirname(__file__), "GetOldTweets3"))

import GetOldTweets3 as got
from twitterscraper import query_tweets_from_user
import pandas as pd

""" Converts all the special unicode values within 
	a string to the correspoding unicode character.
	https://gist.github.com/tushortz/9fbde5d023c0a0204333267840b592f9
""" 
LATIN_1_CHARS = (
    ('\xe2\x80\x99', "'"),
    ('\xc3\xa9', 'e'),
    ('\xe2\x80\x90', '-'),
    ('\xe2\x80\x91', '-'),
    ('\xe2\x80\x92', '-'),
    ('\xe2\x80\x93', '-'),
    ('\xe2\x80\x94', '-'),
    ('\xe2\x80\x94', '-'),
    ('\xe2\x80\x98', "'"),
    ('\xe2\x80\x9b', "'"),
    ('\xe2\x80\x9c', '"'),
    ('\xe2\x80\x9c', '"'),
    ('\xe2\x80\x9d', '"'),
    ('\xe2\x80\x9e', '"'),
    ('\xe2\x80\x9f', '"'),
    ('\xe2\x80\xa6', '...'),
    ('\xe2\x80\xb2', "'"),
    ('\xe2\x80\xb3', "'"),
    ('\xe2\x80\xb4', "'"),
    ('\xe2\x80\xb5', "'"),
    ('\xe2\x80\xb6', "'"),
    ('\xe2\x80\xb7', "'"),
    ('\xe2\x81\xba', "+"),
    ('\xe2\x81\xbb', "-"),
    ('\xe2\x81\xbc', "="),
    ('\xe2\x81\xbd', "("),
    ('\xe2\x81\xbe', ")")
)


def clean_latin1(data):
    
        data = data.decode('iso-8859-1')
        for _hex, _char in LATIN_1_CHARS:
            data = data.replace(_hex, _char)
        return data.encode('utf8')


""" Uses twitterscraper API to fectch all of a users tweets 
	using proxies
"""
def scrapeUsers(username):

    tweetCriteria = got.manager.TweetCriteria().setUsername(username)
                                              

    userTweets = got.manager.TweetManager.getTweets(tweetCriteria)

    """ Clean up tweets by constructing new list with
        tweets that:
        - Are not replies
        - Do not contain media or links
        - Encoded to unicode and converted to python string literal then stripped of
          special char
    """
    cleanUserTweets = []
    for tweet in userTweets:
            cleanTweet = str(clean_latin1(tweet.text.encode(encoding = 'UTF-8')))
            cleanTweet = cleanTweet[2:len(cleanTweet)-1].replace("\\n","").replace("\\","")
            if "xc" not in cleanTweet:
                cleanUserTweets.append(cleanTweet)
                print(cleanTweet)

    return cleanUserTweets

users = ["BASEDSAVAGE_","ogmaxb","uzivurt"]
def main():
	tweets = []
	for user in users: 
		tweets = tweets + scrapeUsers(user)

	dataframe = pd.DataFrame({'tweets': tweets})

	dataframe.to_csv('tweets.csv',encoding='utf-8',index=False,)

if __name__ == '__main__':
	main()