from faker import Faker # Crete fake People
import pandas as pd # Dataframes
import random # random number generation
import requests  # grab web-page
from bs4 import BeautifulSoup as bsopa  #parse web-page
import re # regex parsing
import pymongo as pym

#https://github.com/MrFuguDataScience/MongoDB_notes/blob/master/mongo%20lecture_02.ipynb



"""
I want to generate skills of employees ranging from 1:(1-len(skills) list).
I am generating 500 entries, because I will populate 500 fake prospective employees
to use in my Fake Employment Recruiter Database today.
"""

skills = ['Python','Java','SQL','MongoDB','R','C++','Spark','TensorFlow','skLearn']

def create_rndm_skills(skills):
    random.seed(300) #use to keep data consistent
    randomlist = []
    for i in range(0,500):
        n = random.randint(1,len(skills))
        randomlist.append(n)
    lst_skills_per_person = []
    for i in randomlist:
        lst_skills_per_person.extend([random.sample(skills, i)]) #wow! it takes (i) number of random sample.
    return lst_skills_per_person

fake_ = Faker() #to generate random name!
Faker.seed(413)
fake_name=[]
for i in range(500):
    if i not in fake_name:
        fake_name.append(fake_.name().split(' '))



response=requests.get("https://www.softschools.com/social_studies/state_abbreviations/")

#response.status_code  checking that the request was (ok=200)

soupie = bsopa(response.text,'lxml')  # converting format
html_source=soupie.find('div',{"class":"middlecol"}) # html source code

# tags=html_source.find('a').find_all('href')


# Get US State Abreviations:
table = html_source.find('table', attrs={'class': 'colorBgGreen'})
first_td = table.find('tr')
text = first_td.renderContents()
text_ = text.decode("utf-8")  # convert bytes to string
jj = text_.split('\n')


state_td_tags = []
for i in jj:
    if re.findall(r'\b[A-Z]{2}\b', i):

        #         trr.append(i.replace('<td>','').replace('</td>',''))
        state_td_tags.append(i.replace('<td>', '').replace('</td>', ''))

state_abbr = state_td_tags[:-2]  # the last two lines i didn't need US Territories
# state_abbr


# 500 random US states using, (N CHOOSE K):
state_rnd=random.choices(state_abbr,k=500) # 500 samples. Don't have to iterate 500 times.


# Relocation: (Employee willing to relocate?)
willing_to_relocate=['yes','no','maybe']
relocation_=random.choices(willing_to_relocate,k=500)



# Nested Data:
specialty=['Machine Learning','Data Visualization','Database','Statistics']
experience_level=['Junior','Mid','Senior']

spec_=random.choices(specialty,k=500)
exper_=random.choices(experience_level,k=500)
sp=['specialty']*500
exp=['experience']*500
my_list=list(zip(sp,spec_))
my_list2=list(zip(exp,exper_))



dict_specialty=[{key: value} for (key, value) in my_list] #dict comprehension!


dict_exper=[{key: value} for (key, value) in my_list2]

# This will be our tuple of dictionary pairs:
spec_exp=list(zip(dict_specialty,dict_exper))


# Generating, the full dataset
first_name=[]
last_name=[]
for i in fake_name:
    first_name.append(i[0])
    last_name.append(i[1])
nested_ppl=list(zip(first_name,last_name,create_rndm_skills(skills), state_rnd,spec_exp,relocation_))




cols=['first_name','last_name','skills','state','specialty_exper','relocation']
job_seekers_=pd.DataFrame(nested_ppl,columns=cols,)

pd.DataFrame.to_csv(job_seekers_,'files/job_seekers.csv')
job_seekers_.head()

print(job_seekers_)