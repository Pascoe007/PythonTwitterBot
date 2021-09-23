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

api = tw.API(auth, wait_on_rate_limit=True)


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

    for x in hashTags[0:5]:
        if x[0] != '#':
            index = hashTags.index(x)  
            x = '#' + x
            hashTags[index] = x
        index = hashTags.index(x) 
        hashTags[index] = ''.join(x.split(' '))
            
    print(hashTags[0:5])
    try:
        if today.weekday() == 4 and today.day == 13:
            api.update_status("Is it Friday the 13th Today?\nYes \n\n\n{hashtag}".format(hashtag = ' '.join(hashTags[0:5])))
            print("Tweet Sent", datetime.datetime.now().time())
        else:
                api.update_status("Is it Friday the 13th Today?\nNo \n\n\n{hashtag}".format(hashtag = ' '.join(hashTags[0:5])))
                print("Tweet Sent", datetime.datetime.now().time())   
    except tw.TweepError as e:
        print(e.args[0][0]['code'])
        print(e.args[0][0]['message'])
        time.sleep(900)
        print("Tweet Sent", datetime.datetime.now().time())      
        #schedule.every().day.at(str(hour.strftime("%H:%M"))).do(Tweet)      
        #Tweet()

        

#schedule.every(1).seconds.do(Tweet)
schedule.every().day.at("15:00").do(Tweet)

while True:
    try:
        schedule.run_pending()
    except tw.TweepError as e:
        print(e.args[0][0]['message'])
        time.sleep(10)
        continue
    time.sleep(1)

    



