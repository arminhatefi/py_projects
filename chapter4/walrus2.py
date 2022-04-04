tweet_limit = 280
tweet_string = "Blah" * 100
if (diff := tweet_limit - len(tweet_string)) >= 0:
    print("A fitting tweet", len(tweet_string))
else:
    print("Went over by", abs(diff))
