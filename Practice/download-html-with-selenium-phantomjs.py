from selenium import webdriver

# driver = webdriver.Chrome(executable_path=r'C:\Users\Anonymous\Downloads\chromedriver.exe')

driver = webdriver.PhantomJS(executable_path=r'C:\Users\Anonymous\Downloads\phantomjs-2.1.1-windows\bin\phantomjs.exe')

driver.get('http://python.org')

html_doc = driver.page_source

print(html_doc)