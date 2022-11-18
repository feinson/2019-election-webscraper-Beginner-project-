from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)

#(options=chrome_options)\/
driver = webdriver.Chrome()


central_link = "https://www.bbc.co.uk/news/politics/constituencies"


class Scraper:

    def __init__(self, link):
        driver.get(link)

    def get_links(self):
        link_list=[]
        constituency_div = driver.find_element(by=By.XPATH, value='//*[@id="az_constituency_list"]')
        letter_tables = constituency_div.find_elements(by=By.XPATH, value='./table')

        for letter in letter_tables:
            time.sleep(0.2)
            print(letter.get_attribute('id'))
            tr = letter.find_elements(by=By.XPATH, value='./tbody/tr')
            for row in tr:
                #we can also extract the nation and name here if we want to at a later date
                a_tag = row.find_element(by=By.TAG_NAME, value='a')
                link = a_tag.get_attribute('href')
                link_list.append(link)

        return link_list


    def get_results(self,consituency_page):
        pass
            


if __name__ == '__main__':
    election = Scraper(central_link)
    time.sleep(3)
    print(election.get_links())

