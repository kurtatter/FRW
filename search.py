white_text = """
        def ask():
            answer = input("Привет, как дела?")
            return answer
            
        def again():
            print("слово слово слово слово")
            
        def several():
            print("набор разных русских слов")
            
        def my_in():
            print("в") 
"""

import enum
import re
import string

black_text = """
        def ask():
            answer = input("Hi, how are you?")
            return answer

        def again():
            print("word word word word")

        def several():
            print("several english words")

        def my_in():
            print("in")
"""

reg_rus = re.compile("[а-яА-Я]+")


def is_rus_world(text):
    if not len(list(filter(reg_rus.match, text))):
        return False
    return True


def get_line_number(text):
    for index, line in enumerate(text.split('\n')):
        if is_rus_world(line):
            print(index)

def get_rus_lines(text):
    for index, line in enumerate(text.split('\n')):
        if is_rus_world(line):
            yield (index, line)


def get_rus_words(line):
    return line.split()
    # print(line.split())
    # for word in line:
    #     if is_rus_world(word):
    #         yield word


def get_cleare_text(text):
    text = text.split()
    clear_text = list()
    for i in text:
        clear_text.append(i.split(string.punctuation))
    return clear_text

def get_rus_words(line):
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
        words.append((word, column))
    return words

rus_lines = list(get_rus_lines(white_text))

# print(rus_lines)

for line_number, line in rus_lines:
    for word, column in get_rus_words(line):
        print(f"{word}:{line_number+1}:{column+1}")