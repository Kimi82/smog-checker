import requests
from bs4 import BeautifulSoup
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

URL = 'https://airly.eu/map/pl/#49.82806,19.88781,i1078'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(3)
driver.get(URL)

#title = driver.find_element_by_class_name('sc-iwsKbI fpPHnN')
#driver.close()
soup = BeautifulSoup(driver.page_source, 'html.parser')

#button = soup.find("div", {"class": "sc-htpNat fBJVWQ"})
button2 = driver.find_element_by_xpath("//button[@class='button button--circle ']").click()

