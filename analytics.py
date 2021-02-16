import spacy
from spacy import displacy
import matplotlib
import string

nlp = spacy.load("en_core_web_sm")

with open('skiply.csv', 'r') as f:
    text = f.read().replace('\n', '')

doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label)

text.translate(str.maketrans('', '', string.punctuation))

uniqueWords = []
words = 0
for i in text.strip(' '):
    if i not in uniqueWords:
        uniqueWords.append(i)
    words += 1

print("The total number of words is:", str(words))
print('The number of unique words is:', str(len(uniqueWords)))

displacy.serve(doc, style="dep")
displacy.serve(doc, style="ent")
