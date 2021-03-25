import requests
from bs4 import BeautifulSoup
import socket
import datetime
from random import randint

def get_page():
    # Using the requests module, we use the "get" function
    # provided to access the webpage provided as an
    # argument to this function:
    page = "https://www.goodreads.com/quotes?page="+str(randint(1, 100))
    print('Loading new page ....')
    result = requests.get(page)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    #print(soup.prettify())
    links = soup.find_all('div', {'class' : "quoteText"})
    authors = []
    books = []
    #print(page)
    '''
    authors = soup.find_all('span', {'class' : "authorOrTitle"})
    books = soup.find_all('a', {'class' : "authorOrTitle"})
    #print(links)
    #print("\n")
    '''

    for child in links:
        c = list(child.children)
        #print(c,len(c))
        name = []
        for k in c:
            #print(k)
            if k.name == 'span':
                #print(k.text.strip())
                name.append(k.text.strip())
        #print(name)
        if len(name)>0 : authors.append(name[0])
        if len(name)>1:
            books.append(name[1])
        else:
            books.append('')

    quotes = []

    for link, author, book in zip(links, authors, books):
        l = link.text.strip().split('-')[0].split('\n')
        quote = l[0].replace('“','').replace('”','').replace('\u2014',' ').replace('\u2013',' ').replace('\u2018',' ').replace('\u2019',' ')
        l = (quote, author, book)
        #print(l)
        quotes.append(l)
        #print(quotes, len(quotes))
    return page, quotes

page, quotes = get_page()
n = 0
qotdPortNumber      = 32017;
qotdServerSocket    = socket.socket();
qotdServerSocket.bind(("127.0.0.1", qotdPortNumber));
qotdServerSocket.listen();
print("Quote of the day requests welcome on : ",page);

while(True):
    # accept when client connect on socket
    (socketForClient, clientIP) = qotdServerSocket.accept();
    # Pick a random quote
    quoteIndex      = randint(0,len(quotes)-1);
    quoteOfTheDay   = "%s - %s %s"%(quotes[quoteIndex][0],quotes[quoteIndex][1],quotes[quoteIndex][2]);
    # encode message
    encodedMsg      = quoteOfTheDay.encode(encoding='utf-8');
    # send message
    socketForClient.send(encodedMsg);
    # get time
    timeVal = datetime.datetime.now();
    # report
    print("%s Just served: %s, to client with IP address and port: %s\n\n"%(timeVal, encodedMsg, clientIP));
    # close connection
    socketForClient.close();
    n += 1
    if n == 30 :
        page, quotes = get_page()
        print("New page loaded : ",page);
        n = 0
