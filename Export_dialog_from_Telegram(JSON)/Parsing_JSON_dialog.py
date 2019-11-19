import datetime  # Модуль для отримання часу (для створення унікальних backup файлів)
import inspect  #
import json
import os.path  # Модулі за допомогою яких я створюю паки і отримую шлях до файлу з кодом
import shutil  # Модуль для копіювання файлів (для створення backup файла списку слів)

# ============Условно глобальні змінні
WORD_FILE = 'word_list.txt'
JSON_FILE_NAME = 'result.json'
DIALOG_NAME = 'Рожище'


def backup():
    filename = inspect.getframeinfo(inspect.currentframe()).filename    #
    source_file_path = os.path.dirname(os.path.abspath(filename))       # Визначаємо шлях до файла з виконуваним кодом
    if not os.path.exists(source_file_path + '\\Backup_word'):   # Перевіряємо чи існує папка Backup_word
        os.makedirs(source_file_path + '\\Backup_word')          # Якщо ні, то створюємо папку 'Backup_word' в директорії з виконуваним файлом
    now = datetime.datetime.now()       # Отримуємо поточну дату і час
    time = str(now.year)+'.'+str(now.month)+'.'+str(now.day)+'_'+str(now.hour)+'.'+str(now.minute) # Підганяємо під потрібний нам формат
    backup_file_path = source_file_path+'\\Backup_word\\word_list_backup_' + time + '.txt'  # Зберігаємо назву backup-файла
    shutil.copy2(source_file_path+'\\word_list.txt', backup_file_path)  # Копіюємо файл

def read_from_file(file_name):
    file = open(file_name, 'r', encoding='utf-8')
    line = file.readlines()
    file.close()
    return line


def transfer_to_pair_list(list):
    for iterator in range(len(list)):
        start_index1 = list[iterator].find(')')
        end_index1 = list[iterator].find('-')
        key = list[iterator][start_index1 + 2:end_index1 - 1]
        value = list[iterator][end_index1 + 2:-1]  # Якщо правою гранню зріза встановити -1 то буде братися рядок без \n
        list[iterator] = [key, value]


def writing_to_file(file_name, lines):
    count = 1
    file = open(file_name, 'w', encoding='utf-8')
    for content in lines:
        file.write(str(count) + ') ' + content[0] + ' - ' + content[1] + '\n')
        count += 1
    file.close()


def search_coincidence(list):   # Функція пошуку співпадінь
    for i in range(len(list)):
        for x in range(i+1,len(list)):
            if list[i][0]==list[x][0]:
                print('Coincidences:')
                print(list[i][0],list[i][1])
                print('or')
                print(list[x][0], list[x][1])
                print('Delete first couple? Press 1 and enter.')
                print('Delete second couple? Press 2 and enter.')
                print("Don't make changes? Press 0 and enter.")
                action = input()
                if action=='1':
                    del list[i]
                if action=='2':
                    del list[x]


def main():         # Головна функція
    backup()        # Роблю бекап файлу з попереднім списком слів
    lines = read_from_file(WORD_FILE)  # Відкриваю файл зі списком попередніх слів
    transfer_to_pair_list(lines)  # Перетворюю їх в список типу [key:value] для подальшої роботи з ними
    word_list_from_JSON = []  # Змінна для зберігання JSON-колекції
    file = open(JSON_FILE_NAME, 'r', encoding='utf-8')  # Відкриваємо JSON файл щоб отримати з нього список повідомлень
    content = json.load(file)
    chats_list = content['chats']['list']  # Тут ми отримуємо список всіх чатів
    for dialog in chats_list:  # За допомогою циклу перебираємо список всіх чатів
        if dialog['name'] == DIALOG_NAME:  # Якщо ключ 'name' = 'Назва потрібного чату', то продовжуємо працювати з потрібним діалогом
            message_list = dialog['messages']
            for message in message_list:        #Цикл для перебору всіх повідомлень
                if message['id'] >= 419:  # Передивившись файл вручну знайшов що мені потрібно зберегти всі повідомлення починаючи з 419-го
                    text = '0) ' + message['text'] + '\n'  # Добавляю до строки спереду номер і в кінці перенос на новий рядок щоб використати готову,
                                                           # перевірену функцію 'transfer_to_pair_list()' з файлу Program_to_mention_English_word_console.py
                    word_list_from_JSON.append(text)

    transfer_to_pair_list(word_list_from_JSON)  # Перетворюю список строк в список типу [key:value] для подальшої роботи з ними
    lines = lines + word_list_from_JSON  # Об'єдную дві змінні (попередні слова і нові слова)
    search_coincidence(lines)  # Функція як перевіряє збіги
    writing_to_file(WORD_FILE, lines)  # Записую результат у файл



# ============
main()          # Виклик головної функції
