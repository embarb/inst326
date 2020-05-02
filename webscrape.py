import requests
from bs4 import BeautifulSoup
import time

#web scrape testudo schedule of classes. first get links for all majors and then scrape all course information.

time.sleep(1)
page = requests.get("https://app.testudo.umd.edu/soc/")
soup = BeautifulSoup(page.text, "html.parser")
links = soup.findAll("a")

i = 26
while i < len(links) - 5:
    url = "https://app.testudo.umd.edu/soc/" + links[i]["href"]
    print(url)
    
    #test
    #new_page = requests.get(url)
    #time.sleep(1)
    #new_soup = BeautifulSoup(page.text, "html.parser")
    #info = soup.findAll("div") 
    i += 1
