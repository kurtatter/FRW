"""
This is project for find russion words
in several projects.
Format get data: items
where item: <file_name:line?:column>
"""
import os
import re
import csv

dir_ignore = ['idea', 'venv', 'test', 'git']
r = re.compile("[а-яА-Я]+")
words = ['apple', 'cat', 'яблоко', 'кот', 'building', 'машина', 'status',]


def get_clear_walk_line(walk_line):
    if 'venv' not in walk_line[0] and \
        'idea' not in walk_line[0] and \
        'git' not in walk_line[0] and \
        len(walk_line[0]) > 1:
        return True


def get_ru_word(filename):
    with open(filename) as file:
        text = file.readlines()
        for index, line in enumerate(text):
            if len(list(filter(r.match, line))) != 0:
                print(filename, index+1)
        # print(text)

def get_rus_words(filename):
    with open(filename) as file:
        lines = file.readlines()
        for line_number, line in enumerate(lines):
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
                # words.append((word,line_number+1, column+1, filename))
                # if word: yield (word,line_number+1, column+1, filename)
                if word: yield (word,f"{filename}:{line_number+1}:{column+1}")
                else: continue

def main():
    walklist = list(os.walk('.'))
    files = list()

    clear_walk_list = list()

    for line in walklist:
        if get_clear_walk_line(line):
            clear_walk_list.append(line)

    for line in clear_walk_list:
        # print(line)
        if len(line[2]) != 0:
            for file in line[2]:
                files.append(line[0] + '/' + file)
    # print(files)
    with open("words.csv", "w", newline="") as table:
        tabler = csv.writer(table)
        data = list()
        for file in files:
            # get_ru_word(file)
            for i in get_rus_words(file):
                if not i:
                    continue
                data.append(i)
        tabler.writerows(data)


if __name__ == "__main__":
    main()
