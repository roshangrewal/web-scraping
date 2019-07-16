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



driver = webdriver.Firefox(executable_path=r'C:\Users\Anonymous\Downloads\geckodriver.exe')


