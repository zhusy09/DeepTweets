import GetOldTweets3 as got


user_list = ["BASEDSAVAGE_","ogmaxb"]

def loadTweets(username,count):

	tweetCriteria = got.manager.TweetCriteria().setUsername(username)\
	                                          .setMaxTweets(count)
	tweet_list = got.manager.TweetManager.getTweets(tweetCriteria)

	return tweet_list

def main():

	for user in user_list:
		print(user + " latest tweet ----> ")
		print(loadTweets(user,10)[0].text)



if __name__== "__main__":
	main()