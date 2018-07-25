from bs4 import BeautifulSoup
import requests
import re
import json

mainurl = 'https://www.gla.ac.uk'
subs = json.load(open('scrapers/data/subjectareas.json'))
courses = {}

for c, value in subs.items():
    suburl = value['url']
    r = requests.get(suburl)
    page = r.text
    soup = BeautifulSoup(page, 'html.parser')

    maindiv = soup.find('div', attrs={'class': 'maincontent'})
    course_lists = maindiv.find_all('ul')
    cses = []

    for ul in course_lists:
        cses[0:0] = ul.find_all('a')
    
    for a in cses:
        code = re.findall('[A-Z0-9]+', str(a.attrs['href']))[0]
        courses[code] = {'title': a.attrs['title'], 'url': mainurl + a.attrs['href']}
    
path = 'scrapers/data/courses.json'
f = open(path, 'w+')
json.dump(courses, f)