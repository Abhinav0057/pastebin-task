from os import spawnl
from bs4 import BeautifulSoup as soup
import requests
from selenium import webdriver
import json
  

# import time




#----------------------------------------------------#
#----------------------------------------------------#

# searchquery=input("enter a search query: ")
# print(searchquery)
## Using nepal for now as default 



def callFuncUntillThirty(seatchUrl):
    
    driver = webdriver.Chrome("C:\chromedriver.exe")
    driver.get(searchUrl)
    # time.sleep(5)

    soupPage=soup(driver.page_source, 'html.parser')
    items=[]
    items=soupPage.find_all('div',attrs={'class':'wide-media'})[:30]

   
    return items

def myDataCollection(url):
    while True:
        items=callFuncUntillThirty(url)

        if len(items)==30:
            # filename = "news.csv"
            # f = open(filename, "w",encoding="utf-8")
            f = open('out.json','w',encoding="utf-8")

            # header = "Contains 30 list of news from annapurnam.com\n"
            # f.write(header)
            i=1
            for item in items:
                data={i:(str(item)+'\n')}
                json.dump(data,f )
                i=i+1              
                           
            break
    
        else:
            print(len(items))
            print("Its not 30 data so rereading datas ")
            driver.quit()

    f.close()





if __name__ == "__main__":
    f = open('out.json','w',encoding="utf-8")
  
    searchquery="नेपाल"
    searchUrl="https://annapurnapost.com/search/news?query="+searchquery
    print(searchUrl)
    driver = webdriver.Chrome("C:\chromedriver.exe")
    myDataCollection(searchUrl)










 




 




