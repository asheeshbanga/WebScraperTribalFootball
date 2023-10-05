from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys

application_path = os.path.dirname(sys.executable)

now = datetime.now()
# Date Format - MMDDYYYY
date_string = now.strftime('%m%d%Y')

website = 'https://tribalfootball.com'
path= "/Users/asheesh.banga/Downloads/chrome_driver/chromedriver"

# headless-mode
options = Options()
options.add_argument('--headless=new')

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

containers = driver.find_elements(by="xpath", value='//a[@class="tile tile--slim"]')

titles = []
urls = []

for container in containers:
    title = container.find_element(by='xpath', value='./div/h3').text
    url = container.find_element(by='xpath', value='.').get_attribute("href")
    titles.append(title)
    urls.append(url)

my_dict = {'title': titles, 'url': urls}
df_headlines = pd.DataFrame(my_dict)
file_name = f'headline-{date_string}.csv'
final_path = os.path.join(application_path, file_name)

df_headlines.to_csv(final_path)

driver.quit()