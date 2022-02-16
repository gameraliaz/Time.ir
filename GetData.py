from bs4 import BeautifulSoup
import requests
import re;
import csv;
url="https://time.ir/"
# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content, "lxml")
History=soup.find('ul',class_='list-unstyled')
ListHis=list(map(str,History.find_all('li')))

data=[]
for i in ListHis:
    h=re.split(">|<",i)
    h[6]=h[6].replace('\n','').strip()
    data.append({'day':h[4],'discription':h[6],'holiday':1 if h[1].count("eventHoliday") else 0})
    print(h[6])
with open("data.csv", 'w' , encoding='utf-8-sig' , newline='') as out_file:
    headers = [ 
        "day",
        "discription",
        "holiday"
    ] 
    writer = csv.DictWriter(out_file, headers)
    writer.writeheader()
    writer.writerows(data)
