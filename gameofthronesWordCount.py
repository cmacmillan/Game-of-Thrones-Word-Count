from bs4 import BeautifulSoup
import urllib.request
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


def getHTMLStringFromUrl(url):
	fp = urllib.request.urlopen(url) 
	mybytes = fp.read()
	mystr = mybytes.decode("utf8")
	fp.close() 
	return mystr

def getSeasonAndEpisodeFromString(string):
	return string[98:98+6]

def wordCount(string):
	return len(string.split())	

def charCount(string):
	split = string.split()
	retr=0
	for i in split:
		retr+=len(i)
	return retr

urlFile = open("gameofthronesurls.txt","r")
urls = urlFile.read().split(",")

texts = []
words=[]
chars=[]

episode=[]

counter=0;
for i in urls:
	if (int(getSeasonAndEpisodeFromString(i)[4:])==0):
		continue
	if (getSeasonAndEpisodeFromString(i)=="s07e01"):
		texts.append(("s07e01","a "*4346))
		continue
	soup = BeautifulSoup(getHTMLStringFromUrl(i),'html.parser')
	textbox = soup.findAll("div", {"class":"scrolling-script-container"})[0]
	texts.append((getSeasonAndEpisodeFromString(i),textbox.text))
	counter+=1
	print("finished "+str(counter)+" out of "+str(len(urls)))

counter=0
for i in texts:
	words.append(wordCount(i[1]))
	chars.append(charCount(i[1]))
	episode.append(i[0])

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

"""objects = episode
y_pos = np.arange(len(objects))
performance = words

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Words')
plt.title('Game of Thrones Word Count')

plt.show()
"""
n_groups = 8

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.07
opacity = 0.8
#means


#plt.rcParams.update({'font.size': 13})

episodeIndexWords = []
seasonMean=[]
#episodeIndexWords[Episode][Season]
for i in range(11):
	episodeIndexWords.append([0,0,0,0,0,0,0,0])

for i in range(8):
	seasonMean.append(0)
	episodeCounter=0
	counter=0
	for j in texts:
		season = int(j[0][1:3])-1
		if (season==i):
			episodeCounter+=1
			seasonMean[i]+=words[counter]
		counter+=1
	seasonMean[i]/=episodeCounter


counter=0
for i in texts:
	episode = int(i[0][4:])
	season = int(i[0][1:3])-1
	episodeIndexWords[episode][season] = words[counter]
	counter+=1

rects=[]
for i in range(11):
	if (i==0):
		continue
	rects.append(plt.bar(index+bar_width*i, episodeIndexWords[i], bar_width, alpha=opacity,color=['r','b','g','0.25','m','k','y','c','r','b','y'][i], label='Episode '+str(i)))

plt.xlabel('Episode')
plt.ylabel('Word Count')
plt.title('Game of Thrones Word Count')
plt.tick_params(labelsize=13)
plt.xticks(index + bar_width, ["Season 1","Season 2","Season 3","Season 4","Season 5","Season 6","Season 7","Season 8"])
plt.plot(np.arange(8)+.5,seasonMean,label="Season Mean")
plt.legend()


plt.tight_layout()
plt.show()
