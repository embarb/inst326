import requests
from bs4 import BeautifulSoup
import time
import coursescrape

#web scrape testudo schedule of classes. first create list of majors of courses. then create urls for each course. finally, extract
#info from each section of courses.
time.sleep(1)
page = requests.get("https://app.testudo.umd.edu/soc/")
soup = BeautifulSoup(page.text, "html.parser")
major_links = soup.findAll("a")

url_list = []
course_list = []

i = 11
while i < len(major_links) - 5:
    url = "https://app.testudo.umd.edu/soc/" + major_links[i]["href"]
    url_list.append(url)
    i += 1


for url in url_list:
    course_url = coursescrape.course_scrape(url)
    course_list.append(course_url)
    
for course in course_list:
    coursescrape.section_scrape(course)
