from bs4 import BeautifulSoup
import json
import urllib
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from selenium.common.exceptions import NoSuchElementException

with open('url_sowtfare_testing_loc_bangalore.json','r') as f:
    url = json.load(f)
data ={}    

i = 1
jd_df = pd.DataFrame()

driver = webdriver.Firefox(executable_path=r'C:\Users\Anonymous\Downloads\geckodriver.exe')


for u in url:
    driver.wait = WebDriverWait(driver, 2)
    driver.maximize_window()
    driver.get(u)
#    r = urllib.urlopen(u).read()
    soup = BeautifulSoup(driver.page_source, "lxml")
#    jd_df['position'] =
#    print soup
    try:
        header = soup.find("div",{"class":"header cell info"})
        position = driver.find_element_by_xpath('//*[@id="HeroHeaderModule"]/div[3]/div[1]/div[2]/div[1]/h2').text
        company = driver.find_element_by_xpath('//*[@id="HeroHeaderModule"]/div[3]/div[1]/div[2]/span[2]').text
        location = driver.find_element_by_xpath('//*[@id="HeroHeaderModule"]/div[3]/div[1]/div[2]/span[3]').text
        jd_temp = soup.select('div.jobDescriptionContent.desc')
        jd = jd_temp[0].text
    #    website = soup.find("span",{"class":"value website"}).get_text()
        info = soup.find_all("infoEntity")
    except IndexError:
        print('IndexError: list index out of range')

    except NoSuchElementException:
        pass


    data[i] = {
        'url' :u,
        'Position': position,
        'Company': company,
        'Location' :location,
#        'website':website,
#        'revenue' :revenue,
#        'competitors' :competitors,
        'Job_Description' :jd
    }
    print(i)
    i+=1 
    
driver.quit()
jd_df = pd.DataFrame(data)
jd = jd_df.transpose()
#cols = jd.columns.tolist()
#print cols
jd = jd[['url','Position','Company','Location','Job_Description']]
jd.to_csv('jd_software_testing.csv',encoding="utf-8")