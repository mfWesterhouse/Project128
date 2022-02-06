from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser = webdriver.Chrome('chromedriver.exe')
browser.get(START_URL)
time.sleep(10)
headers = ["name", "distance", "mass", "radius"]
star_data = []
new_star_data = []

def scrape():
    soup = BeautifulSoup(browser.text, 'html.parser')
    star_table = soup.find_all('table')
    table_rows = star_table[7].find_all('tr')
    temp_list = []

    for tr_tag in soup.find_all("tr", attrs={"class": "fact_row"}):
            td_tags = tr_tag.find_all("td")
            for td_tag in td_tags:
                try:
                    temp_list.append(td_tag.find_all("div", attrs={"class": "fact_row"})[0].contents[0])
                except:
                    temp_list.append("")
    new_star_data.append(temp_list)
scrape()

for index, data in enumerate(star_data):
    scrape(data[5])
    print(f"{index+1} page 2 done")
final_star_data = []
for index, data in enumerate(star_data):
    new_star_data_element = new_star_data[index]
    new_star_data_element = [elem.replace("\n", "") for elem in new_star_data_element]
    new_star_data_element = new_star_data_element[:7]
    final_star_data.append(data + new_star_data_element)
with open("final.csv", "w") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(final_star_data)