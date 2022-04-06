from bs4 import BeautifulSoup as bs
import requests


def getsoup():
    url='https://www.geeksforgeeks.org/python-programming-language/'
    req_txt=requests.get(url)
    return bs(req_txt.content,'html.parser')


def getcontent1(soup):
    content=soup.find('div',class_='entry-content')
    return content.find_all('p')


def getcontent2(soup):
    s=soup.find('div',id='main')
    leftbar=s.find('ul', class_='leftBarList')
    content=leftbar.find_all('li')
    return content

def printres(res):

    for r in res:
        print(r.text)


def scrapgkg():
    soup=getsoup()
    print(soup.prettify())
    print("#########CONTENT#########")
    content = getcontent1(soup)  #based on div class name
    # content = getcontent2(soup)    #based on div id
    # print(content)
    print("#########RESULT#########")
    printres(content)




if __name__=='__main__':
    scrapgkg()