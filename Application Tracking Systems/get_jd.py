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

with open('url.json','r') as f:
    url = json.load(f)
data ={}    

i = 1
jd_df = pd.DataFrame()

driver = webdriver.Firefox(executable_path=r'C:\Users\Anonymous\Downloads\geckodriver.exe')


for u in url:
    driver.wait = WebDriverWait(driver, 5)
    driver.maximize_window()
    driver.get(u)
#    r = urllib.urlopen(u).read()
    soup = BeautifulSoup(driver.page_source, "lxml")
#    jd_df['position'] =
#    print soup
    header = soup.find("div",{"class":"header cell info"})
    position = driver.find_element_by_xpath('//*[@id="HeroHeaderModule"]/div[3]/div[1]/div[2]/div[1]/h2').text
    company = driver.find_element_by_xpath('//*[@id="HeroHeaderModule"]/div[3]/div[1]/div[2]/span[2]').text
    location = driver.find_element_by_xpath('//*[@id="HeroHeaderModule"]/div[3]/div[1]/div[2]/span[3]').text
    jd_temp = soup.select('div.jobDescriptionContent.desc')
    jd = jd_temp[0].text
#    website = soup.find("span",{"class":"value website"}).get_text()
    info = soup.find_all("infoEntity")
    try:    
        headquaters = info[1].find_element_by_class_name("span",{"class":"value"}).get_text().strip().strip('\\u')
        employees = info[2].find_element_by_class_name("span",{"class":"value"}).get_text().strip().strip('\\u')
        founded = info[3].find_element_by_class_name("span",{"class":"value"}).get_text().strip().strip('\\u')
        industry = info[5].find_element_by_class_name("span",{"class":"value"}).get_text().strip().strip('\\u')
    #     driver.findElement(By.xpath("//input[@id='gh-ac']")).sendKeys("Guitar"); // xpath
    # driver.findElement(By.xpath("//input[@id='gh-ac']")).sendKeys("Guitar");


    except:
        headquaters = None
        employees = None
        founded = None
        industry = None
#    revenue = info[6].find("span",{"class":"value"}).get_text().strip()
#    competitors = info[7].find("span",{"class":"value"}).get_text().strip()    
    data[i] = {
        'url' :u,
        'company': company,
        'position': position,
        'location' :location,
#        'website':website,
        'headquaters':headquaters,
        'employees':employees,
        'founded' :founded,
        'industry' :industry,
#        'revenue' :revenue,
#        'competitors' :competitors,
        'Job Description' :jd
    }
    print(i)
    i+=1 
    
driver.quit()
jd_df = pd.DataFrame(data)
jd = jd_df.transpose()
#cols = jd.columns.tolist()
#print cols
jd = jd[['company','position','url','location','headquaters','employees','founded','industry','Job Description']]
print(jd)
jd.to_csv('data_30thJune.csv',encoding="utf-8")