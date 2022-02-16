from bs4 import BeautifulSoup
import requests
import re;
url="https://time.ir/"

def GetListOfEvents():
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")
    History=soup.find('ul',class_='list-unstyled')
    ListHis=list(map(str,History.find_all('li')))
    data=[]
    for i in ListHis:
        h=re.split(">|<",i)
        h[6]=h[6].replace('\n','').strip()
        data.append({'day':h[4],'discription':h[6],'holiday':1 if h[1].count("eventHoliday") else 0})
    return data




