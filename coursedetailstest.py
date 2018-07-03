from bs4 import BeautifulSoup
import requests
import re
import json

url = 'https://www.gla.ac.uk/coursecatalogue/course/?code=COMPSCI2007'
r = requests.get(url)
page = r.text
soup = BeautifulSoup(page, 'html.parser')

levels = {'Level 1 (SCQF level 7)': 1, 'Level 2 (SCQF level 8)': 2, 'Level 3 (SCQF level 9)': 3, 'Level 4 (SCQF level 10)': 4, 'Level 5 (SCQF level 11)': 5}
semesters = {'Semester 1': 1, 'Semester 2': 2, 'Runs Throughout Semesters 1 and 2': 3, 'Either Semester 1 or Semester 2': 4}
bools = {'Yes': True, 'No': False}

maindiv = soup.find('div', attrs={'class': 'maincontent'})
title_code = maindiv.find('h1').text
tc_list = title_code.split()
title = " ".join(tc_list[0:len(tc_list)-1])
code = tc_list[-1]
coursedetail = {}
geninfo = maindiv.find_all('li')
infos = [code, title]
keys = ['code', 'title', 'session', 'school', 'credits', 'level', 'offeredin', 'visiting', 'erasmus']
for li in geninfo:
    l = li.text.split(': ')
    if l[1] in levels.keys():
        infos.append(levels[l[1]])
    elif l[1] in semesters.keys():
        infos.append(semesters[l[1]])
    elif l[1] in bools.keys():
        infos.append(bools[l[1]])
    else:
        if l[0] == 'Credits':
            infos.append(int(l[1]))
        else:
            infos.append(l[1])

coursedetail = dict(zip(keys, infos))
print(infos)
for k, v in coursedetail.items():
    print(k, v)
