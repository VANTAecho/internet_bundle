import tweepy

# Authenticate (fill in with your keys)
api_key = "YOUR_API_KEY"
api_secret = "YOUR_SECRET"
access_token = "YOUR_TOKEN"
access_secret = "YOUR_ACCESS"

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
api = tweepy.API(auth)

# Tweet message
tweet = "Start your business with $3. Join the EchoVanta economy now. https://echovanta.co/start"
api.update_status(tweet)
print("Tweet sent!")
