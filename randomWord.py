import urllib2 
import random

"""global variable for list of random words"""
wordlist= []
listlen=5000

def Randomwordgenerator():
	"""parses text file to create list of random words"""
	html = urllib2.urlopen("https://raw.githubusercontent.com/mahsu/IndexingExercise/master/5000-words.txt")
	html=html.read()
	index=0
	while(len(wordlist) < listlen):
		wordlist.append(html[index: html[index:].find("\n")])
		html = html[html[index:].find("\n")+1:]
	return None

def findword():
	"""randomly selects a word from wordlist"""
	x=random.randint(0,listlen-1)
	return wordlist[x]

def checkinlist(word):
	"""checks if a given word is in the list"""
	return word in wordlist

def addtolist(word):
	"""adds word to wordlist"""
	wordlist.append(word)
	listlen=listlen+1
	return wordlist(listlen-1) + "added to list"





if __name__ == '__main__':
	Randomwordgenerator()
	print findword()
	print findword()
	print findword()
	print findword()
	print findword()
	print findword()
	print findword()
	print findword()
	#print checkinlist("devote")
	#print checkinlist("farm")
	#print checkinlist("aaaaaaabbbskljd")
