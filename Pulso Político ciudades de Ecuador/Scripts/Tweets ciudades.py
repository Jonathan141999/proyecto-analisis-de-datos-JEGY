
import sys
import couchdb
from tweepy import Stream 
from tweepy import OAuthHandler 
from tweepy.streaming import StreamListener 
import json


###API ########################
ckey = "tIaMOe2pYntmwLT3JLU89ETW7"
csecret = "qzIWvghjvQx9THMMxGQ3TdG2amAhPqLUu8ra3G9BTwH3J8N776"
atoken = "1110505230498705408-2iPeM8DRO3R5yec1OH51WIEI6j7j3Z"
asecret = "mkHAf4xlJmY4uOfYkzw0MwKP8zeIzU0ZYLz2TfKUwCCp6"
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
    db = server.create('guaranda')
except:
    db = server('guaranda')


#twitterStream.filter(locations=[-0.225219,-78.5248])    
#CRITERIO DE FILTRACIÓN
#/twitterStream.filter(track=['Ecuador','Quito','Pulso Politico','Elecciones','Candidatos','Presidencia','Diputados'])
#/twitterStream.filter(track=['Ecuador','Guayaquil','Pulso Politico','Elecciones','Candidatos','Presidencia','Diputados'])
#/twitterStream.filter(track=['Ecuador','Manta','Pulso Politico','Elecciones','Candidatos','Presidencia','Diputados'])
#/#twitterStream.filter(track=['Ecuador','Babahoyo','Pulso Politico','Elecciones','Candidatos','Presidencia','Diputados'])
#/twitterStream.filter(track=['Ecuador','Cuenca','Pulso Politico','Elecciones','Candidatos','Presidencia','Diputados'])
#/twitterStream.filter(track=['Ecuador','Loja','Pulso Politico','Elecciones','Candidatos','Presidencia','Diputados'])
#/twitterStream.filter(track=['Ecuador','Chone','Pulso Politico','Elecciones','Candidatos','Presidencia','Diputados'])
#/twitterStream.filter(track=['Ecuador','Esmeraldas','Pulso Politico','Elecciones','Candidatos','Presidencia','Diputados'])
#/twitterStream.filter(track=['Ecuador','Los Ríos','Pulso Politico','Elecciones','Candidatos','Presidencia','Diputados'])
#/twitterStream.filter(track=['Ecuador','Tulcán','Pulso Politico','Elecciones','Candidatos','Presidencia','Diputados'])
#/twitterStream.filter(track=['Ecuador','Machala','Pulso Politico','Elecciones','Candidatos','Presidencia','Diputados'])
#/twitterStream.filter(track=['Ecuador','Ambato','Pulso Politico','Elecciones','Candidatos','Presidencia','Diputados'])
#/twitterStream.filter(track=['Ecuador','Tena','Pulso Politico','Elecciones','Candidatos','Presidencia','Diputados'])
#/twitterStream.filter(track=['Ecuador','Salinas','Pulso Politico','Elecciones','Candidatos','Presidencia','Diputados'])
#/twitterStream.filter(track=['Ecuador','Santo Domingo','Pulso Politico','Elecciones','Candidatos','Presidencia','Diputados'])
#/twitterStream.filter(track=['Ecuador','Villamil','Pulso Politico','Elecciones','Candidatos','Presidencia','Diputados'])
#/twitterStream.filter(track=['Ecuador','Otavalo','Pulso Politico','Elecciones','Candidatos','Presidencia','Diputados'])
#/twitterStream.filter(track=['Ecuador','Latacunga','Pulso Politico','Elecciones','Candidatos','Presidencia','Diputados'])
twitterStream.filter(track=['Ecuador','Guaranda','Pulso Politico','Elecciones','Candidatos','Presidencia','Diputados'])

