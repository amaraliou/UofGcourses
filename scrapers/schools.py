from bs4 import BeautifulSoup
import requests
import re
import json

mainurl = 'https://www.gla.ac.uk'
schoolsurl = mainurl + '/coursecatalogue/browsebyschool/'

r = requests.get(schoolsurl)
page = r.text
soup = BeautifulSoup(page, 'html.parser')

schoolsoup = soup.find('div', attrs={'class': 'maincontent'})
schools_html = schoolsoup.find_all('a')

schools = {}

for subject in schools_html:
    code = re.findall('[A-Z0-9]+', str(subject.attrs['href']))[0]
    schools[code] = {'title': subject.attrs['title'], 'url': mainurl + subject.attrs['href']}

for k, v in schools.items():
    print(k, v)

f = open('data/schools.json', 'w+')
json.dump(schools, f)