from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import codecs

# Initialize Chrome driver instance
driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

# Navigate to the url
driver.get('https://pythonexamples.org/tmp/selenium/index.html')
get_url = driver.current_url
print("The current url is:"+str(get_url))

#Redirect
val = input("Enter a url: ")
wait = WebDriverWait(driver, 10)
driver.get(val)
wait.until(EC.url_to_be(val))
page_source = driver.page_source

soup = BeautifulSoup(page_source,features="html.parser")
title = soup.title.text
file=codecs.open('article_titles.txt', 'a+')
file.write(title+"\n")
file.close()

get_url = driver.current_url 
print("The current url is:"+str(get_url))

val = input("Enter a url: ")
wait = WebDriverWait(driver, 10)
driver.get(val)
wait.until(EC.url_to_be(val))
page_source = driver.page_source
soup2 = BeautifulSoup(page_source,features="html.parser")
title = soup2.title.text
file=codecs.open('article_titles.txt', 'a+')
file.write(str(title)+"\n")
file.close()

get_url = driver.current_url 
print("The current url is:"+str(get_url))
driver.quit()