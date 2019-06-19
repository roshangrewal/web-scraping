from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import json
from bs4 import BeautifulSoup
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Firefox(executable_path=r'C:\Users\Anonymous\Downloads\geckodriver.exe')
#driver.get('http://inventwithpython.com')

#driver = webdriver.Firefox()
def openbrowser(locid, key):
    driver.wait = WebDriverWait(driver, 5)
    driver.maximize_window()
    words = key.split()
    txt =''    
    for w in words:
        txt +=(w+'+')
#    print txt
    driver.get("https://www.glassdoor.co.in/Job/jobs.htm?suggestCount=0&suggestChosen=true&clickSource=searchBtn&typedKeyword={}&sc.keyword={}&locT=C&locId={}&jobType=".format(txt[:-1],txt[:-1], locid))
    return driver
#s = urllib.urlopen('file:///C:/UTA/Data%20Science/Project2/pokemon_5378/data/{}/{}'.format(folder,files)).read()
def geturl(driver):
    url = set()
    while True:    
        soup1 = BeautifulSoup(driver.page_source, "lxml")
        
        main = soup1.find_all("li",{"class":"jl"})
        
        for m in main:
            url.add('https://www.glassdoor.co.in{}'.format(m.find('a')['href']))
            print(len(url))

        print(url)
        # next_element = soup1.find("li",{"class":"next"})
        # next_exist= next_element.find('a')
        try:
            next_element = soup1.find("li", {"class": "next"})
            try:
                next_exist = next_element.find('a')
            except AttributeError:
                driver.quit()
                break
            except NoSuchElementException:
                driver.quit()
                break
            if next_exist:
    #            driver.find_element_by_xpath(".//*[@id='FooterPageNav']/div/ul/li[7]/a").click()
                driver.find_element_by_class_name("next").click()
                time.sleep(2)
            else:
                driver.quit()
                break
        except ElementClickInterceptedException:
            pass
        # except AttributeError:
        #     pass
    return list(url)

x =openbrowser(locid =2940587, key='Data Scientist')
with open('url_data_scientist_loc-bangalore6.json','w') as f:
    json.dump(geturl(driver),f, indent = 4)
