import requests
from bs4 import BeautifulSoup
import re
import csv
import os

URL = 'https://deliveroo.co.uk/faq'
page = requests.get(URL)

# The following creates a BeautifulSoup object  with the url from the page var.
# You also tell it to use the appropriate parser
soup = BeautifulSoup(page.content, 'html.parser')

# pprint.pprint(soup.prettify)

# finding the appropriate element that has all the job listings using the id
results = soup.find(class_='ccl-4c92e28b43e557eb ccl-85b2395f51210087')
source = results.text

# creating question and answer list and initialising title to be used in csv
questions = []
questions.append('Question')
answers = []
answers.append('Answer')

faqQuestion = results.find_all('h3')

for i in faqQuestion:
    questions.append(i.text)

# replacing questions in the source for easy regex
for i in questions:
    if i in source:
        source = source.replace(i, 'REGULAREX')

answerRegex = re.compile(r'EX(.*?)REGULAR', re.DOTALL)
for i in answerRegex.findall(source):
    answers.append(i)

# creating a csv file and then adding the questions and answers
with open('deliveroo.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(zip(questions, answers))

with open('deliveroo.csv', 'r') as f:
    deliverooText = f.read()

# replacing deliveroo with skiply
with open('skiply2.csv', 'w') as f:
    f.write(re.sub(r'(deliveroo|Deliveroo|DELIVEROO)', 'Skiply', deliverooText))

os.remove('deliveroo.csv')
