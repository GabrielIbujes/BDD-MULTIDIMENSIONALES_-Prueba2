
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API ########################
ckey = "6Zyv4XxVypDqHDpFoHwSTrMzX"
csecret = "3J5TpltHtmEZGEw8RhRLABc3KQ2Quhjj2SVVykfw5zs02fjtpC"
atoken = "153168970-C8H0rPCjztDmLQMrjtgOYSPIzjLMyegrtrAZQQrq"
asecret = "WxWpMOMlghN1tVYZRFugRWTefM1SShLWVI4lL4oPWTAlO"
#####################################

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://admin:admin@localhost:5984/')  #('http://115.146.93.184:5984/')
try:
    db = server.create('bd1')
except:
    db = server['bd1']
    
'''===============LOCATIONS=============='''    

twitterStream.filter(locations=[-74.25909,40.477399,-73.700181,40.916178])  
#twitterStream.filter(track=['newyork'])