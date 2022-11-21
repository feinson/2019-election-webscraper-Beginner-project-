from bs4 import BeautifulSoup
import time
import pandas as pd
import requests


# #chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument("--headless") # Runs Chrome in headless mode.
# chrome_options.add_argument('--no-sandbox') # Bypass OS security model
# chrome_options.add_argument('--disable-gpu')  # applicable to windows os only
# chrome_options.add_argument('start-maximized') # 
# chrome_options.add_argument('disable-infobars')
# chrome_options.add_argument("--disable-extensions")

#(options=chrome_options)\/



central_link = "https://www.bbc.co.uk/news/politics/constituencies"


class Scraper:

    def __init__(self, link):
        self.central_link = link
        pass

    def get_links_names_nations(self):
        name_list, nation_list, link_list =[], [], []

        response = requests.get(self.central_link)
        soup = BeautifulSoup(response.content, "html.parser")
        letter_tables = soup.find_all("table", class_ = 'az-table')

        for letter in letter_tables:
            #print(letter.get('id'))
            trs = letter.find_all("tr", class_ = 'az-table__row')
            for row in trs:
                a_tag = row.find('a')
                name = a_tag.get_text()
                name_list.append(name)
                
                n_tag = row.find("td")
                nation = n_tag.get_text()
                nation_list.append(nation)
                
                link = a_tag['href']
                link =f"https://www.bbc.co.uk{link}"
                link_list.append(link)
                #print(name,nation,link)
                
                

        return [name_list, nation_list, link_list]


    def get_results(self,consituency_page):

        #con, lab, ld, green, brexit, snp, pc, dup, sdlp, uup, alliance, other = [0,0,0,0,0,0,0,0,0,0,0,0]
        #if we wanted to add detailed party results data we could extract it this way

        response = requests.get(consituency_page)
        soup = BeautifulSoup(response.content, "html.parser")
        headline = soup.find("p", class_='ge2019-constituency-result-headline__text')
        result = headline.get_text()

        full_result_list = soup.find("ol", class_='ge2019-constituency-result__list')
        party_zones = full_result_list.find_all('li', recursive = False)
        

        party_name_list = []
        votes_list = []
        for party_frame in party_zones:
            #print(party_frame)
            party_name_container = party_frame.find('span', class_ = 'ge2019-constituency-result__party-name')
            party_name = party_name_container.get_text()
            party_name_list.append(party_name)

            vote_container = party_frame.find('span', class_ = 'ge2019-constituency-result__details-value')
            v = vote_container.get_text()
            v = v.replace(",","")
            v=int(v)
            votes_list.append(v)
        # I extracted the whole list of party's so that later if I want to add detailed party results, I can
        first_party, second_party =party_name_list[0:2]

        mp_container = full_result_list.find('span', class_ = 'ge2019-constituency-result__candidate-name')
        mp = mp_container.get_text()
        #print(mp)

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

    

    data.to_csv("./data_folder/election_results_scraped.csv")
