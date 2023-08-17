from textblob import TextBlob
import tweepy
import sys

api_key="GqwVml66K9r0gEexociUfvehO"
api_key_secret="GiJWedY9BTPF7jzbIiP864CFYkbIWZs4Mb5lLsnpd6WEdzXeyz"
access_token="1538398742801440769-2qyUa8v10qBBZmHVUqNwFbROjJCuN8"
access_token_secret="tMz0cVWTNUmi3LSX4zLgqd0zvw33GeKBUQmNmLAgULwZd"

auth_handler=tweepy.OAuthHandler(consumer_key=api_key,consumer_secret=api_key_secret)
auth_handler.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth_handler)

search_term="apple"
tweet_amount=250

tweets=tweepy.Cursor(api.search_tweets,q=search_term,lang='en').items(tweet_amount)

polarity=0
positive=0
neutral=0
negative=0
for tweet in tweets:
    final_text=tweet.text.replace("RT"," ")
    if final_text.startswith(" @"):
        position=final_text.index(":")
        final_text=final_text[position+2:]
    if final_text.startswith("@"):
        position=final_text.index(" ")
        final_text=final_text[position+2:]
    analysis=TextBlob(final_text)
    polarity=analysis.polarity
    polarity+=1
    if analysis.polarity>0:
        positive+=1
    elif analysis.polarity<0:
        negative+=1
    elif analysis.polarity==0:
        neutral+=1
    print(final_text," ",polarity)


