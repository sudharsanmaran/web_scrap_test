from bs4 import BeautifulSoup as bs
import requests


def getsoup():
    url='https://www.geeksforgeeks.org/python-programming-language/'
    req_txt=requests.get(url)
    return bs(req_txt.content,'html.parser')


def getcontent1(soup):
    content=soup.find('div',class_='entry-content')
    return content

def getcontent2(soup):
    content=soup.find('div',id='')
    return content

def printres(res):

    for r in res:
        print(r.text)


def divid(content):
    res = content.find_all()

def getres(content):
    return content.find_all('p')

def scrapgkg():
    soup=getsoup()
    print(soup.prettify())
    print("#########CONTENT#########")
    content = getcontent1(soup)  #based on div class name
    # content = getcontent2(soup)    #based on div id
    print(content)
    res=getres(content)
    print("#########RESULT#########")
    printres(res)




if __name__=='__main__':
    scrapgkg()