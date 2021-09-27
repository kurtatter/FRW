import string
import re

reg_rus = re.compile("[а-яА-Я]+")

line = '            answer = input("Привет, как дела?")'


words = list()
carret = 0
while re.search("[а-яА-Я]+", line):
    match = re.search("[а-яА-Я]+", line)
    # print(match.group())
    word = match.group()
    carret += match.end()
    column = carret - len(match.group())
    # print(carret)
    line = line[match.end():]
    words.append((word, column) )

print(words)
line = '            answer = input("Привет, как дела?")'

for w, c in words:
    print(line[c:c+len(w)])
