from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

central_link = "https://www.bbc.co.uk/news/politics/constituencies"
driver = webdriver.Chrome()
driver.get(central_link)
time.sleep(3)

constituency_div = driver.find_element(by=By.XPATH, value='//*[@id="az_constituency_list"]')
letter_tables = constituency_div.find_elements(by=By.XPATH, value='./table')
letter = letter_tables[0]

trs = letter.find_elements(by=By.XPATH, value='./tbody/tr')
row = trs[0]

n_tag = row.find_element(by=By.TAG_NAME, value='td')
print(n_tag.text.strip())