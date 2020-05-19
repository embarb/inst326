import requests
from bs4 import BeautifulSoup
import time

def course_scrape(url):
    #obtain course urls
    time.sleep(1)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    links = soup.findAll('div', class_="course-id")
    
    for link in links:
        course_url = url + "/" + link.text
        return course_url
        
def section_scrape(url):
    time.sleep(1)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    
    #section information
    sections = soup.findAll('span', class_="section-id")
    instructors = soup.findAll('span', class_="section-instructor")
    days = soup.findAll('span', class_="section-days")
    start_times = soup.findAll('span', class_="class-start-time")
    end_times = soup.findAll('span', class_="class-end-time")
    discussions = soup.findAll('span', class_="class-type")
    buildings = soup.findAll('span', class_="building-code")
    rooms = soup.findAll('span', class_="class-room")
