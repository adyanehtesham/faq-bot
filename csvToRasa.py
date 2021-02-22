import pandas

df = pandas.read_csv('skiply.csv')
questions = df.Question
answers = df.Answer

nlu = open('/rasa/data/nlu.yml', 'a')
domain = open('/rasa/domain.yml', 'a')
stories = open('rasa/data/stories.yml', 'a')

for i in range(len(questions)):
    intent = "".join(u for u in questions[i] if u not in ("?", ".", " ", "’", "-", "+", "(", ")", "'"))
    nlu.write('- intent: {0}\n  examples: |\n       - {1}\n\n'.format(
        intent, questions[i]))
    domain.write("- {0}\n".format(intent))

nlu.close()

domain.write("responses:\n")

for i in range(len(questions)):
    intent = "".join(u for u in questions[i] if u not in ("?", ".", " ", "’", "-", "+", "(", ")", "'"))
    answer = answers[i].replace('\n', ' ').replace(':', '')
    domain.write("  utter_{0}:\n    - text: {1}\n".format(intent, answer))

domain.write("actions:\n")
for i in range(len(questions)):
    intent = "".join(u for u in questions[i] if u not in ("?", ".", " ", "’", "-", "+", "(", ")", "'"))
    domain.write("- utter_{0}\n".format(intent))

domain.close()

for i in range(len(questions)):
    intent = "".join(u for u in questions[i] if u not in ("?", ".", " ", "’", "-", "+", "(", ")", "'"))
    stories.write('\n- story: {0}\n  steps:\n   - intent: {1}\n   - action: utter_{1}\n'.format(intent, intent))

stories.close()
