import urllib2 
import random
"""Class Contains findFirstLink which is used to find a path to the philosophy page 
and pathLength which determines how many clicks to get to philosophy page"""
wordlist= []
def Randomwordgenerator():
	html = urllib2.urlopen("https://raw.githubusercontent.com/docdis/english-words/master/words2.txt")
	html=html.read()
	index=0
	while(len(wordlist) < 4000):
		wordlist.append(html[index: html[index:].find("\n")])
		html = html[html[index:].find("\n")+1:]

def findword():
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

