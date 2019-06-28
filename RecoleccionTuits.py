import tweepy
import csv
import pandas as pd
from pandas import ExcelWriter
####input your credentials here
consumer_key = 'XXXXXXXXXXXXX'
consumer_secret = 'XXXXXXXXXXXXX'
access_token ='XXXXXXXXXXXXX'
access_token_secret = 'XXXXXXXXXXXXX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)


listaCreados=[]
listatwets=[]
#25-26 esp 
#Feminism
for tweet in tweepy.Cursor(api.search,q="#Feminismo",
                           lang="es",
                           since="2019-06-01",until="2019-06-02").items():
    listatwets.append(tweet.text.encode('utf-8').decode("utf-8"))
    listaCreados.append(tweet.created_at)
 
df = pd.DataFrame({'Creado':listaCreados,'Tweets':listatwets})
df = df[['Creado','Tweets']]
header = ['Creado','Tweets']

df.to_csv('Feminismo.csv',mode='a', index=False,encoding='utf-8-sig' )
#writer.save()
