from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd
import requests
import io
from PIL import Image

# list_of_rows = ["Andover", "Birmingham", "Canterbury", "Devizes"]

# andover_list = ["conservative", "liz truss"]
# birmingham_list = ["lib dem", "nick clegg"]
# canterbury_list = ["labour", "jeremy corbyn"]
# devizes_list = ["snp", "nicola sturgeon"]

# data = pd.DataFrame({"names":list_of_rows,  # Create pandas DataFrame
#                      "party":range(0,4),
#                      "mp":range(0,4)})



# data.iloc[0, 1:] = andover_list
# data.iloc[1, 1:] = birmingham_list
# data.iloc[2, 1:] = canterbury_list
# data.iloc[3, 1:] = devizes_list

# print(data)

# data.to_csv("./data_folder/testy.csv")

chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.theyworkforyou.com/mp/elizabeth_truss/")
img_frame = driver.find_element(by=By.TAG_NAME, value="img")

link = img_frame.get_attribute("src")
img_content = requests.get(link).content
img_file = io.BytesIO(img_content)
img = Image.open(img_file)
file_path = "./data_folder/mp_photos_list/elizabeth_truss.jpg"

with open(file_path, "wb") as f:
    img.save(f, "JPEG")