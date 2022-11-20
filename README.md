# Data Collection Pipeline

This github repo representes my first foray into the world of webscraping. It currently includes a python script which uses selenium to scrape the results of the 2019 UK General Election from the BBC website.

## Election Scraper with Selenium
This script first opens the A-Z Consituency list on the BBC website and extracts the link to the page of each constituency in the UK. It then cycles through each link, pulling the results of the election.
The output is a csv file that contains the following headings:
- Constituency (name of)
- Nation
- Link
- Result
- First party
- Second Party
- MP
- Total votes
- Votes for winner

## Next: Re-write with BeautifulSoup?
I'm considering re-writing the script with BeautifulSoup and eschewing the whole selenium thing because the script is currently very slow and takes more than 10 minutes to scrape the data from all 250 constituencies.