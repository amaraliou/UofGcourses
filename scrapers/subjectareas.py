from bs4 import BeautifulSoup
import requests
import re
import json

mainurl = 'https://www.gla.ac.uk'
subjectsurl = mainurl + '/coursecatalogue/browsebysubjectarea/'

r = requests.get(subjectsurl)
page = r.text
soup = BeautifulSoup(page, 'html.parser')

subjectmain = soup.find('div', attrs={'class': 'maincontent'})
subs_html = subjectmain.find_all('a')

subjectareas = {}

for subject in subs_html:
    code = re.findall('[A-Z]+', str(subject.attrs['href']))[0]
    subjectareas[code] = {'title': subject.attrs['title'], 'url': mainurl + subject.attrs['href']}

for k, v in subjectareas.items():
    print(k, v)

f = open('scrapers/data/subjectareas.json', 'w+')
json.dump(subjectareas, f)