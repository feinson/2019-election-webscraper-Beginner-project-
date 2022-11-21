from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd


chrome_options = Options()
# #chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument("--headless") # Runs Chrome in headless mode.
# chrome_options.add_argument('--no-sandbox') # Bypass OS security model
# chrome_options.add_argument('--disable-gpu')  # applicable to windows os only
# chrome_options.add_argument('start-maximized') # 
# chrome_options.add_argument('disable-infobars')
# chrome_options.add_argument("--disable-extensions")

#(options=chrome_options)\/
driver = webdriver.Chrome(options=chrome_options)


central_link = "https://www.bbc.co.uk/news/politics/constituencies"


class Scraper:

    def __init__(self, link):
        driver.get(link)

    def get_links_names_nations(self):
        name_list=[]
        nation_list=[]
        link_list=[]

        constituency_div = driver.find_element(by=By.XPATH, value='//*[@id="az_constituency_list"]')
        letter_tables = constituency_div.find_elements(by=By.XPATH, value='./table')

        for letter in letter_tables:
            
            #print(letter.get_attribute('id'))
            trs = letter.find_elements(by=By.XPATH, value='./tbody/tr')
            for row in trs:
                a_tag = row.find_element(by=By.TAG_NAME, value='a')
                name = a_tag.get_attribute('text')
                name_list.append(name)
                
                n_tag = row.find_element(by=By.XPATH, value='./td')
                nation = n_tag.get_attribute('textContent')
                nation_list.append(nation)
                
                link = a_tag.get_attribute('href')
                link_list.append(link)
                
                
                

        return [name_list, nation_list, link_list]


    def get_results(self,consituency_page):

        #con, lab, ld, green, brexit, snp, pc, dup, sdlp, uup, alliance, other = [0,0,0,0,0,0,0,0,0,0,0,0]
        #if we wanted to add detailed party results data we could extract it this way

        driver.get(consituency_page)
        time.sleep(0.1)
        headline = driver.find_element(by=By.XPATH, value = '//*[@id="constituency_result_headline2019"]/div/div[1]/div[1]/p')
        result = headline.get_attribute('textContent')
        full_result_list = driver.find_element(by=By.XPATH, value = '//*[@id="constituency_result_table2019"]/div/ol')
        party_zones = full_result_list.find_elements(by=By.XPATH, value = './li')


        party_name_list = []
        votes_list = []
        for party_frame in party_zones:
            party_name_container = party_frame.find_element(by=By.CLASS_NAME, value = 'ge2019-constituency-result__party-name')
            party_name_list.append(party_name_container.get_attribute('textContent'))

            vote_container = party_frame.find_element(by=By.CLASS_NAME, value = 'ge2019-constituency-result__details-value')
            v = vote_container.get_attribute('textContent')
            v = v.replace(",","")
            v=int(v)
            votes_list.append(v)
        
        first_party, second_party =party_name_list[0:2]

        mp_container = full_result_list.find_element(by=By.CLASS_NAME, value = 'ge2019-constituency-result__candidate-name')
        mp = mp_container.get_attribute('textContent')

        total_votes = sum(votes_list)
        votes_for_winner =votes_list[0]

        return  [result, first_party, second_party, mp, total_votes, votes_for_winner]



        


if __name__ == '__main__':
    election = Scraper(central_link)
    triple_list = election.get_links_names_nations()
    sixfifty = len(triple_list[0])

    data = pd.DataFrame({"#":range(1,sixfifty+1),  # Create pandas DataFrame
                        "ONS ID":range(1,sixfifty+1),
                        "Constituency":triple_list[0],
                        "Nation":triple_list[1],
                        "Link":triple_list[2],
                        "Result":range(0,sixfifty),
                        "First party":range(0,sixfifty),
                        "Second party":range(0,sixfifty),
                        "MP":range(0,sixfifty),
                        "Total votes":range(0,sixfifty),
                        "Votes for winner":range(0,sixfifty)})
    
    for i, link in enumerate(triple_list[2]):
        res = election.get_results(link)
        ons_id = link.split("/").pop()
        data.iloc[i,1] = ons_id
        data.iloc[i,5:]=res
        print(triple_list[0][i])

    data.to_csv("election_results_scraped.csv")

    data.to_csv("./data_folder/election_results_scraped.csv")
