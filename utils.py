def sliceTweet (text : str):
    words = text.split(' ')
    tweet = ""
    tweets = []
    for word in words:
        if len(tweet) + len(word) <= 280:
            tweet += word + ' '
        else:
            tweets.append(tweet)
            tweet = ""
    
    return tweets