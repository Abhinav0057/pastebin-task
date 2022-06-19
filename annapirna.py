from os import spawnl
from bs4 import BeautifulSoup as soup
import requests
from selenium import webdriver

# import time




#----------------------------------------------------#
#----------------------------------------------------#

# searchquery=input("enter a search query: ")
# print(searchquery)
## Using nepal for now as default 

searchquery="नेपाल"
searchUrl="https://annapurnapost.com/search/news?query="+searchquery
print(searchUrl)




driver = webdriver.Chrome("C:\chromedriver.exe")

def callFuncUntillThirty():
    
    driver = webdriver.Chrome("C:\chromedriver.exe")
    driver.get(searchUrl)
    # time.sleep(5)

    soupPage=soup(driver.page_source, 'html.parser')
    items=[]
    items=soupPage.find_all('div',attrs={'class':'wide-media'})[:30]
   
    return items


while True:
    items=callFuncUntillThirty()

    if len(items)==30:
        filename = "news.csv"
        f = open(filename, "w",encoding="utf-8")

        header = "Contains 30 list of news from annapurnam.com\n"
        f.write(header)
        for item in items:
            f.write(str(item) )
            f.write('\n')
            
            driver.close()
            break
    
    else:
        print(len(items))
        print("Its not 30 data so rereading datas ")
        driver.close()

f.close()





# print(htmlPage.content)
# soupPage = soup(htmlPage, 'html5lib')

# print(items)



# for item in items:
#      print(1)

 




