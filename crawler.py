from html.parser import HTMLParser
#parser- htmli alam moodul, eraldus punktiga
from urllib.request import urlopen
from urllib import parse

url = "www.delfi.ee"

class LinkParser(HTMLParser):

    def handle_starttag(self,tag, attrs):
        if tag == 'a':
            for(key,value) in attrs:
                if key == 'href':
                    newUrl = parse.urljoin(self.baseurl, value)
                    self.links + [newUrl]
    def getLinks(self,url):
        self.url=[]
        self.baseUrl = url
        response = urlopen(url)
        if response.getheader('Content-type')=='text/html':
            htmlBytes = response.read()
            htmlString = htmlBytes.decode("utf-8")
            self.feed(htmlString)
            return htmlString, self.links
        else:
            return "",[]
    def spider(url, word, maxPages):
        pagesToVisit=[url]
        numberVisit = 0
        foundWord = False
        while numberVisited < maxPages and pageToVisit != [] and not foundWord:
            numberVisited = numberVisited+1
            url = pageToVisit[0]
            pageToVisit = pageToVisit[1:]
            try:
                print(numberVisited, "Visiting", url)
                parser = LinkParser()
                data,links = parser.getLinks()
                if data.find(word)> -1:
                    foundword = True
                    pageToVisit = pageToVisit + links
                    print("Õnnetus!")
            except:
                    print("Halvasti läks")
            if foundWord:
                    print ("Sõna", word, "leidsime aadressilt", url)
            else:
                    print("Sellist sõna ei leitud")
                   

LinkParser.spider("www.neti.ee",200)

     
                    
            
                    