import urllib2
import re
import bs4

symbolfile = open("ted_talk_transcript.txt")
symbolslist = symbolfile.read()
newsymbolslist = symbolslist.split("\n")
i=0

wr= open("Result.txt",'wb')
while i<len(newsymbolslist):
    url="https://www.ted.com/talks/"+newsymbolslist[i]+"/transcript?language=en"
    web_page = urllib2.urlopen(url)
    page_text = web_page.read()
    soup = bs4.BeautifulSoup(page_text)
    list = soup.findAll('div', attrs={'class':'talk-article__body talk-transcript__body'})
    text = [t.get_text().encode('utf-8') for t in list]
    for item in text:
    	wr.write("%s\n" % item)
    print (newsymbolslist[i],"transcript fetched !!")
    i+=1
    
