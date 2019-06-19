from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from helpers import search_jobs
from helpers import read_listings
import random
import pickle


# create a new Firefox session
driver = webdriver.Firefox(executable_path=r'C:\Users\Anonymous\Downloads\geckodriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()

#define job posting search
#these inputs can be changed!
url = "https://www.glassdoor.co.in/index.htm"
job_title_input = "Data Scientist"
location_input = "Bangalore (India)"

#url='https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=true&clickSource=searchBtn&typedKeyword=data+sc&sc.keyword=data+scientist&locT=C&locId=1127927&jobType='
driver.get(url)

#call search_jobs function
search_jobs(driver, job_title_input, location_input)

#initialize loop variables
idx = 1
results = {}

#find total number of job postings
job_count = int(driver.find_element_by_class_name("jobsCount").text[:-5].replace(',', ''))
# driver.find_element_by_xpath("/html/body/div[12]/div/div[2]/div/div[1]").click()

while True:
    #let user know the scraping has started
    print("starting round")
    #find job listing elements on web page
    listings = driver.find_elements_by_class_name("jl")
    #read through job listings and store index and results
    idx, results = read_listings(driver, listings, idx, results)
    #find "next" button to go to next page of job listings
    next_btn = driver.find_element_by_class_name("next")
    #if there is no next button, finish the search
    if len(next_btn.find_elements_by_class_name("disabled ")) != 0:
        print("end of search, final index: " + str(idx))
        break
    #if the job listing index is higher than the total number of job postings found from the search, finish the search
    if idx > job_count:
        break
    #click the next button
    next_btn.click()
    #tell webdriver to wait until it finds the job listing elements on the new page
    WebDriverWait(driver, 5).until(lambda driver: driver.find_elements_by_class_name("jl"))
    #let the user know how many job listings have been scraped
    print("end of round, new index: " + str(idx))

#archive search using pickle
with open('results.pickle', 'wb') as handle:
    pickle.dump(results, handle, protocol=pickle.HIGHEST_PROTOCOL)

jd = df['company', 'description', 'location', 'title']
jd.to_csv('data_2nd_June.csv',encoding="utf-8")


# close the browser window
driver.quit()