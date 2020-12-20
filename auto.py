import tweepy
import os
import time
from dotenv import load_dotenv
import random

env_path = '.env'
load_dotenv(dotenv_path=env_path)
SECRET_KEY = os.getenv("MODEL_TASK_ID")


consumer_key         = os.getenv("CONSUMER_KEY")
consumer_secret      = os.getenv("CONSUMER_SECRET")
access_token_key     = os.getenv("ACCES_TOKEN")
access_token_secret  = os.getenv("ACCES_TOKEN_SECRET")
USERNAME_FESS_TARGET = os.getenv("USERNAME_FESS_TARGET").split(',')
MINUTES = 60


auth = tweepy.OAuthHandler(consumer_key , consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)
AUTH_USER_ID = api.me().id




def isAlreadySave(id_str):
    tweetExist = False
    with open('ids.txt', 'r') as f:
        ids = f.read().split(',')
        if id_str in ids:
            tweetExist = True
    
    return tweetExist

def writeTweetId(id_str):
    if isAlreadySave(id_str) == True:
        return False
    
    with open('ids.txt', 'a') as f:
        f.write(str(id_str)+",")
        
    return True

def followUser(api, user_id):
    stat = api.show_friendship(source_id = AUTH_USER_ID, target_id=user_id)[0]
    if stat.following == False and stat.following_requested == False:
        api.create_friendship(user_id=user_id)
        print('succes following')
    else:
        print('already following or pending reqs')



if __name__ == '__main__':
    print('STARTING.....')
    while True:
        data = api.user_timeline(screen_name=random.choice(USERNAME_FESS_TARGET),
                     count= 1)
        tweet_id = data[0].id_str
        if writeTweetId(tweet_id) == False:
            print('already grab this twt, sleep for 10 minutes')
            time.sleep(10 * MINUTES)

            continue

        people_rt_ids = api.retweeters(tweet_id)
        for i in range(4):
            #4 times action per call RT's tweet detail
            id_to_follow = random.choice(people_rt_ids)
            followUser(api, id_to_follow)
            print('sleep for 5 minutes....')
            time.sleep(5 * MINUTES)



        time.sleep(10 * MINUTES)
        print('sleep for 10 minutes....')