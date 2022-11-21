# Data Collection Pipeline

This github repo representes my first foray into the world of webscraping. It currently includes a python script which uses selenium to scrape the results of the 2019 UK General Election from the BBC website.

## Election Scraper with Selenium
This script 'selenium_scraper.py' first opens the A-Z Consituency list on the BBC website and extracts the link to the page of each constituency in the UK. It then cycles through each link, pulling the results of the election. It puts these results into a pandas dataframe.
The output is a csv file that contains the following headings:
- ONS ID
- Constituency (name of)
- Nation
- Link
- Result
- First party
- Second Party
- MP
- Total votes
- Votes for winner

## Election Scraper with BeautifulSoup
I added a second script 'soup_scraper.py' that provides exactly the same functionality as the first, but uses the BeautifulSoup library rather than Selenium. The result of this is that this script is much much faster.

## soup_scraper_with_photos.py
This script has the additional functionality of downloading a photo for each MP from their profile picture on www.streetlist.co.uk. Currently there is a problem with the Northern Irish constituencies since there are no profile pictures for Northern Irish MPs on www.streetlist.co.uk. This could be solved by potentially finding a better source of the photos

## Test script
Please ignore the test script. I use it to muck around and test stuff. I will get rid off it eventually.

## Data folders
Running the scripts outputs files to the data_folder and mp_photos_list directories.