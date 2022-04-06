from bs4 import BeautifulSoup as bs
import requests


def getsoup():
    url='https://www.geeksforgeeks.org/python-programming-language/'
    req_txt=requests.get(url)
    return bs(req_txt.content,'html.parser')


def getcontent(soup):
    content=soup.find('div',class_='entry-content')
    return content


def printresult(content):
    res = content.find_all('p')
    for r in res:
        print(r.text)


def scrapgkg():
    soup=getsoup()
    print(soup.prettify())
    print("##################")
    content = getcontent(soup)
    print(content)
    print("##################")
    printresult(content)



if __name__=='__main__':
    scrapgkg()