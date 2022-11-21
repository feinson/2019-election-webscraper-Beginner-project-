import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests


response = requests.get('https://www.bbc.co.uk/news/politics/constituencies/W07000049')
soup = BeautifulSoup(response.content, "html.parser")

full_result_list = soup.find("ol", class_='ge2019-constituency-result__list')
party_frames=full_result_list.find_all('li', recursive = False)
print(party_frames[0])

# chrome_options = Options()
# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.theyworkforyou.com/mp/elizabeth_truss/")
# img_frame = driver.find_element(by=By.TAG_NAME, value="img")

# link = img_frame.get_attribute("src")
# img_content = requests.get(link).content
# img_file = io.BytesIO(img_content)
# img = Image.open(img_file)
# file_path = "./data_folder/mp_photos_list/elizabeth_truss.jpg"

# with open(file_path, "wb") as f:
#     img.save(f, "JPEG")