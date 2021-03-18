import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API ########################
ckey = "BQ56nvxNrt3a7xeNEbLCYV4Bz"
csecret = "52e1nSrv0BA6DPeQwEVqCXaRaM2H6tnbR2SffcuYPUZgTc8zAM"
atoken = "711211480264396801-kyuyyls0BxT7I4m0MlQjS3wUhNvbotn"
asecret = "osWJrMlKQl9UbHpdWVrQmcyXc19E6NXJmSvKpoDfw6JXX"
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
server = couchdb.Server('http://Guillo9977:guillo07@localhost:5984/')  
try:
    db = server.create('pichincha')
except:
    db = server('pichincha')


twitterStream.filter(locations=[-79.3709,-0.7211,-77.8397,0.3273])    
#CRITERIO DE FILTRACIÓN
twitterStream.filter(track=['Guillermo Lasso','2021','presidente','CREO'])
