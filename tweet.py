import tweepy
consumer_key= ""
consumer_secret=""
access_token = ""
access_token_secret = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
while True:
    enter_user = input("Enter user:")
    userID = enter_user
    api = tweepy.API(auth)
    tweets = api.user_timeline(screen_name=userID, count=140, include_rts = False, tweet_mode = 'extended'
                           )
    for info in tweets[:]:
        print(info.created_at)
        print(info.full_text)
        print("\n")
    x = input("Want to continue(y/n): ")
    if x == "y":
        continue
    else:
        break