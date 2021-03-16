
import sys
import couchdb
from tweepy import Stream #autentica las credenciales
from tweepy import OAuthHandler #
from tweepy.streaming import StreamListener #hereda la clase 
import json


###API ########################
ckey = "X1cHhuKlzjY6eUQ2J6i4MuVUR"
csecret = "kEd5yq95noDC726oYSGYSXkuF4S71kj2IFauS3qmOGIDQHJ7XC"
atoken = "1339966381102665730-uXm8t9BvPwJk6z2JYjIsD0f6RT3f3i"
asecret = "3AxhyMbXhL43J4cUFssbZAFpIIqS92tqOjSYLJbC4jqIi"
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
server = couchdb.Server('http://Jonathan14:Familia141999@localhost:5984/')  #('http://115.146.93.184:5984/')
try:
    db = server.create('cotopaxigl')
except:
    db = server('cotopaxigl')
    
'''===============LOCATIONS=============='''    

#Filtro por geolocalización
twitterStream.filter(locations=[-79.3393,-1.22,-78.3809,-0.3308])
#Filtro por palabras
#twitterStream.filter(track=['Elecciones Ecuador 2021','Andres Arauz','CENTRO'])
twitterStream.filter(track=['Elecciones Ecuador 2021','Guillermo Lasso','CREO'])
