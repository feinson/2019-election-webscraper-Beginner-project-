# Data Collection Pipeline

This github repo representes my first foray into the world of webscraping. It currently includes a python script which uses selenium to scrape the results of the 2019 UK General Election from the BBC website.

## Election Scraper with Selenium
This script first opens the A-Z Consituency list on the BBC website and extracts the link to the page of each constituency in the UK. It then cycles through each link, pulling the results of the election. It puts these results into a pandas dataframe.
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

## Image scraping
I added a second script that, additionally to scraping the election results, takes the name of the MP and then goes to www.theyworkforyou.com and downloads the profile picture for each MP, based on looking for their name from the BBC results. Currently it runs into a slight issue if the BBC's name of the MP does not match the name of the MP on www.theyworkforyou.com (for example - "Chris" vs "Christopher"). It also runs into a slight issue if, like in the case of "David Davies", there are multiple profiles for that name on www.theyworkforyou.com. Both these cases are handed with try/except statements and the image for that MP is simply not downloaded. According to my testing the script pulled images for 612/650 MPs elected in 2019.

## Test script
Please ignore the test script. I use it to muck around and test stuff. I will get rid off it eventually.

## Data folders
Running the scripts outputs files to the data_folder and mp_photos_list directories.