import pymongo
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


ckey = "6Zyv4XxVypDqHDpFoHwSTrMzX"
csecret = "3J5TpltHtmEZGEw8RhRLABc3KQ2Quhjj2SVVykfw5zs02fjtpC"
atoken = "153168970-C8H0rPCjztDmLQMrjtgOYSPIzjLMyegrtrAZQQrq"
asecret = "WxWpMOMlghN1tVYZRFugRWTefM1SShLWVI4lL4oPWTAlO"


class listener(StreamListener):

    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
            doc = mycol.insert_one(dictTweet)
            print("SAVED" + str(doc) + "=>" + str(data))
        except:
            print("Already exists")
            pass
        return True

    def on_error(self, status):
        print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''Mmongo'''

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb=myclient["bdd3"]
mycol = mydb["bdd3"]

'''===============LOCATIONS=============='''


twitterStream.filter(track=['Donald Trump'])

