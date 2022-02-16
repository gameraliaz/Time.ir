from bs4 import BeautifulSoup
import requests
import re;

def ListOfMonthEvents(year,month):
    url=f"https://www.time.ir/fa/event/list/0/{year}/{month}"
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

def ListOfCurrentYearEvents():
    url="https://www.time.ir/fa/eventyear-%d8%aa%d9%82%d9%88%db%8c%d9%85-%d8%b3%d8%a7%d9%84%db%8c%d8%a7%d9%86%d9%87"
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")
    History=soup.find_all('ul',class_='list-unstyled')
    Data=[]
    for i in range(12):
        ListHis=list(map(str,History[i].find_all('li')))
        data=[]
        for i in ListHis:
            h=re.split(">|<",i)
            h[6]=h[6].replace('\n','').strip()
            data.append({'day':h[4],'discription':h[6],'holiday':1 if h[1].count("eventHoliday") else 0})
        Data.append(data)
    return Data


def ListOfCurrentMonthEvents():
    url="https://time.ir/"
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