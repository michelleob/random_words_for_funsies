import urllib2 
import random

"""global variable for list of random words"""
wordlist= []

def Randomwordgenerator():
	"""parses text file to create list of random words"""
	html = urllib2.urlopen("https://raw.githubusercontent.com/docdis/english-words/master/words2.txt")
	html=html.read()
	index=0
	while(len(wordlist) < 4000):
		wordlist.append(html[index: html[index:].find("\n")])
		html = html[html[index:].find("\n")+1:]

def findword():
	"""randomly selects a word from wordlist"""
	x=random.randint(0,3999)
	return wordlist[x]



if __name__ == '__main__':
	print Randomwordgenerator()
	print findword()
	print findword()
	print findword()
	print findword()
	print findword()
	print findword()
	print findword()
	print findword()

