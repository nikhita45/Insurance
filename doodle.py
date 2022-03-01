import pandas as pd
import requests 
from bs4 import BeautifulSoup
import json

#URL = "https://www.google.com/doodles"
URL = "https://www.google.com/doodles/json/1999/10?h1=en"
data =  requests.get(URL) 

word = data.json()
table1 = pd.DataFrame(word)


for j in range(2000,2022):
    for i in range(1,13):
        url = ("".join(["https://www.google.com/doodles/json/",str(j),"/",str(i),"?hl=en"]))
        link = requests.get(url)
        words = link.json()
        table2 = pd.DataFrame(words)
        #print(table2)

        table1 = pd.concat([table1,table2])


print(table1.info())
table1.to_csv('table1.csv')


'''
#from selenium import webdriver
#from BeautifulSoup import BeautifulSoup
import pandas as pd
import requests 
from bs4 import BeautifulSoup 


def getdata(url): 
    r = requests.get(url) 
    return r.text 
    
htmldata =  requests.get("https://www.google.com/doodles") 
soup = BeautifulSoup(htmldata.content, 'html.parser') 

#

image_no = 0
for item in soup.find_all('img'):
    image_no += 1
    print(item['src'])
print(image_no)
#print(htmldata.content)
'''   