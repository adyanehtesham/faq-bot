# you can get the questions by using regex
# each question starts with "QUESTION:" and ends with </br>
# get the data and store it in a file
# use regex to filter out everything else
# keep "QUESTION:" so you can use regex or something to store qyestions and
# their respective answers.

import requests
from bs4 import BeautifulSoup
import re
import csv
import os

URL = 'https://help.uber.com/ubereats/article/dine-in-and-pick-up-order-faq?nodeId=dceda7b6-cc5a-4351-beae-b87ae7c28de9'
page = requests.get(URL)

# Creating a BeautifulSoup object
soup = BeautifulSoup(page.content, 'html.parser')

# Element with all the faqs
results = soup.find(class_='layout__item desk-and-up-four-fifths')

# finds all the individual faq elements
faqQuestion = results.find_all('span')

# writing to a file to be processed later
text = open('uberEats.txt', 'w')
for i in faqQuestion:
    text.write(i.text + '\n')
text.close()

# getting all the text in one string variable
with open("uberEats.txt", 'r') as f:
    uberEats_txt = f.readlines()
whole_txt = "".join(uberEats_txt)

# regex stuff, seperating questions and answers
# creating question and answer list and initialising title to be used in csv
questions = []
questions.append('Question')
answers = []
answers.append('Answer')
questionRegex = re.compile(r'QUESTION:.*\?')
answerRegex = re.compile(r'\?(.*?)QUESTION', re.DOTALL)

for i in questionRegex.findall(whole_txt):
    questions.append(i)

for i in answerRegex.findall(whole_txt):
    answers.append(i)

# removing uneccessasry items.
for i in answers:
    i = i.replace('\n', ' ')
    i = i.replace('. . .', '')

# creating a csv file and then adding the questions and answers
with open('uber.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(zip(questions, answers))

# Replacing instances of uber with skiply
with open('uber.csv', 'r') as f:
    uberText = f.read()
with open('skiply1.csv', 'w') as f:
    f.write(re.sub('Uber', 'Skiply', uberText))

# Removing the 'QUESTION:' before every question
with open('skiply1.csv', 'r') as f:
    skiply1Text = f.read()
with open('skiply1.csv', 'w') as f:
    f.write(re.sub('QUESTION:', '', skiply1Text))

# Deleting unnecessary files
os.remove('uberEats.txt')
os.remove('uber.csv')
