import pandas as pd
from textblob import TextBlob
import re
import emoji
import unicodedata
import csv
import numpy as np
import sys
import nltk 
import string
import codecs
import matplotlib.pyplot as plt


df = pd.read_csv('Feminismo.csv', encoding = 'utf8')
first = df["Tweets"]
print(len(first))


# Emojis pattern
emoji_pattern = re.compile("["
						u"\U0001F600-\U0001F64F"  # emoticons
						u"\U0001F300-\U0001F5FF"  # symbols & pictographs
						u"\U0001F680-\U0001F6FF"  # transport & map symbols
						u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
						u"\U00002702-\U000027B0"
						u"\U000024C2-\U0001F251"
						u"\U0001f926-\U0001f937"
						u'\U00010000-\U0010ffff'
						u"\u200d"
						u"\u2640-\u2642"
						u"\u2600-\u2B55"
						u"\u23cf"
						u"\u23e9"
						u"\u231a"
						u"\u3030"
						u"\ufe0f"
			"]+", flags=re.UNICODE)

normal=[]
positivo=[]
negativo=[]

largodf= len(first)
i=0


for sentence in a.sentences:
	print(sentence.sentiment.polarity)

while(i < 980):
	a= emoji_pattern.sub(r'', first[i]) # no emoji

	blob = TextBlob(a)
	a = str(blob.translate(to="en") )
	wiki = TextBlob(a)

	for sentence in wiki.sentences:
		if(sentence.sentiment.polarity==0.0):
			normal.append(sentence.sentiment.polarity)
		elif(sentence.sentiment.polarity<0):

			negativo.append(sentence.sentiment.polarity)
		elif(sentence.sentiment.polarity>0):
			positivo.append(sentence.sentiment.polarity)


	i=i+1



print(sum(normal)/len(normal))
print(sum(positivo)/len(positivo))
print(sum(negativo)/len(negativo))

labels = 'Positivo', 'Negativo','Normal'
sizes = [len(positivo),len(negativo),len(normal)]
colors = ['gold', 'lightcoral', 'lightskyblue']
explode = (0.1, 0.1, 0.1)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()

