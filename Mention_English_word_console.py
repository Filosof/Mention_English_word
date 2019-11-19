import os  # Підключаю для виклику системної функції system('cls')
import random

# ========== Условно глобальні змінні
FILE_PATH = r'D:\Programming_all\Python\PyCharm_project_\Program_to_mention_English_word\word_list.txt'


def read_from_file(file_name):
    file = open(file_name, 'r', encoding='utf-8')
    line = file.readlines()
    file.close()
    return line


def writing_to_file(file_name, lines):
    count = 1
    file = open(file_name, 'w', encoding='utf-8')
    for content in lines:
        file.write(str(count) + ') ' + content[0] + ' - ' + content[1] + '\n')
        count += 1
    file.close()


def transfer_to_pair_list(list):
    for iterator in range(len(list)):
        start_index1 = list[iterator].find(')')
        end_index1 = list[iterator].find('-')
        key = list[iterator][start_index1 + 2:end_index1 - 1]
        value = list[iterator][end_index1 + 2:-1]  # Якщо правою гранню зріза встановити -1 то буде братися рядок без \n
        list[iterator] = [key, value]


def get_random_pair(list):
    pair = random.choice(list)
    return pair


def from_english(pair):
    print('Please enter a translation : ' + pair[0])
    input()
    print('Right answer : ' + pair[1])


def from_ukraine(pair):
    print('Please enter a translation : ' + pair[1])
    input()
    print('Right answer : ' + pair[0])


def add_new_pair(lines):
    print('Enter English word : ')
    key = input()
    print('Enter Ukrainian translate : ')
    value = input()
    lines.append([key, value])


def main():
    lines = read_from_file(FILE_PATH)
    transfer_to_pair_list(lines)

    mode = input('Ukrainian => English press 1\nEnglish => Ukrainian press 2\n')
    print("======================================\n")
    count = 1  # Лічильник повторених слів
    length = len(lines)  # Загальна кілікість слів
    while (len(lines) > 0):
        if mode == '1':
            word = get_random_pair(lines)
            from_ukraine(word)
            lines.remove(word)
        else:
            word = get_random_pair(lines)
            from_english(word)
            lines.remove(word)
        print("=============== Amount of repeating word:" + str(count) + " of " + str(length) + "\n")
        print('')
        count += 1



# ==================
main()      # Виклик головної функції