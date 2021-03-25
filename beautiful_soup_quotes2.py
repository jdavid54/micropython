import requests
from bs4 import BeautifulSoup
import socket
import datetime
from random import randint

# Using the requests module, we use the "get" function
# provided to access the webpage provided as an
# argument to this function:
page = "https://www.goodreads.com/quotes?page="+str(randint(1, 100))
result = requests.get(page)
src = result.content
soup = BeautifulSoup(src, 'lxml')
#print(soup.prettify())


print(page)
links = soup.find_all('div', {'class' : "quoteText"})
authors = []
books = []

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
        
    #print('*******************************')


authors = soup.find_all('span', {'class' : "authorOrTitle"})
books = soup.find_all('a', {'class' : "authorOrTitle"})
#print(links)
#print("\n")
'''
# Perhaps we just want to extract the link that has contains the text
# "About" on the page instead of every link. We can use the built-in
# "text" function to access the text content between the <a> </a>
# tags.
quotes = []


for link, author, book in zip(links, authors, books):
    l = link.text.strip().split('-')[0].split('\n')
    quote = l[0]#.replace('“','').replace('”','').replace('\u2014',' ').replace('\u2013',' ').replace('\u2018',' ').replace('\u2019',' ')
    l = (quote, author, book)
    #print(l)
    quotes.append(l)
#print(quotes, len(quotes))
print(page)
for q in quotes:
    #print(q[0])
    enc = q[0].encode(encoding='utf-8')
    #print(enc)
    #print(enc.decode(encoding='latin8'))
'''    
for n in range(100):  #8192
    b = str(chr(128+n))
    #print(b, end='')
    print(b.encode(encoding='utf-8'),b)