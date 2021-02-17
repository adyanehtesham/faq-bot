import spacy
from spacy import displacy
from matplotlib import pyplot
import string
from collections import Counter

nlp = spacy.load("en_core_web_sm")

with open('skiply.csv', 'r') as f:
    text = f.read().replace('\n', '')

doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label)

text.translate(str.maketrans('', '', string.punctuation))

print("The total number of words is:", str(words))

displacy.serve(doc, style="dep")
displacy.serve(doc, style="ent")

# Getting a list of tuples for the occurrences of all the words
# Extracting the data of the 10 most common words and then plotting that
# to a bar graph using pyplot.
freq = Counter(text.split())
popular = freq.most_common(10)
length = len(popular)

pyplot.bar(range(length), [length[1] for length in popular], align='center')
pyplot.xticks(range(length), [length[0] for length in popular])

pyplot.show()
