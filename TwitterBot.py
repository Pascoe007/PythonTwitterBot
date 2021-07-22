import tweepy as tw
import datetime
import schedule
import time
import config


print("APP Started")
APIKey = config.APIKey
APISKey = config.APISKey
bearerToken = config.bearerToken
accessToken = config.accessToken
accessTokenSecret = config.accessTokenSecret

woeid = 23424975

auth = tw.OAuthHandler(APIKey, APISKey)
auth.set_access_token(accessToken, accessTokenSecret)

api = tw.API(auth)


def Tweet():
    woeid = 23424975
    trends = api.trends_place(id = woeid)
    hashTags =[] 
    for value in trends:
        for trend in value['trends']:
            hashTags.append(trend['name'])

    trends = api.trends_place(id = woeid)
    today = datetime.datetime.now()
    todaystr = today.strftime("%H:%M:%S")    

    

    for x in hashTags[0]:
        if x[0] != '#':  
            if today.weekday() == 4 and today.day == 13:
                api.update_status("Is it Friday the 13th Today?\nYes \n\n\n{hashtag}".format(hashtag = x))
                print("Tweet Sent")
                
            else:
                api.update_status("Is it Friday the 13th Today?\nNo \n\n\n{hashtag}".format(hashtag = x))
                print("Tweet Sent")
        

#schedule.every(5).seconds.do(Tweet)
schedule.every().day.at("15:00").do(Tweet)

while True:
    schedule.run_pending()
    time.sleep(1)

    



